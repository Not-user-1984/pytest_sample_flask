def test_create_event(client, init_database):
    # Тест на создание события.
    # Отправляется POST-запрос на создание события с датой 2024-01-21, названием "Test Event" и текстом "This is a test event".
    response = client.post(
        '/api/v1/calendar/',
        data="2024-01-21|Test Event|This is a test event")
    # Проверяем, что код ответа равен 201, что означает успешное создание ресурса.
    assert response.status_code == 201
    # Проверяем, что в ответе содержится строка "new id:", указывающая, что было создано новое событие.
    assert b"new id:" in response.data


def test_list_events(client, init_database):
    # Тест на получение списка событий.
    # Отправляется GET-запрос для получения всех событий из календаря.
    response = client.get('/api/v1/calendar/')
    # Проверяем, что код ответа равен 200, что означает успешное выполнение запроса.
    assert response.status_code == 200
    # Проверяем, что в данных ответа содержится ранее добавленное событие с датой 2024-01-21, названием "Test Event" и текстом "This is a test event".
    assert b"2024-01-21|Test Event|This is a test event" in response.data


def test_read_event(client, init_database):
    # Тест на чтение конкретного события по его ID.
    # Отправляется GET-запрос для получения события с ID 1.
    response = client.get('/api/v1/calendar/1/')
    # Проверяем, что код ответа равен 200, что означает успешное выполнение запроса.
    assert response.status_code == 200
    # Выводим ответ для отладки (необязательно, но полезно).
    print(response)
    # Проверяем, что в данных ответа содержится событие с датой 2024-01-21, названием "Test Event" и текстом "This is a test event".
    assert b"2024-01-21|Test Event|This is a test event" in response.data


def test_update_event(client, init_database):
    # Тест на обновление события.
    # Отправляется PUT-запрос для обновления события с ID 1 новыми данными: дата 2024-01-22, название "Updated Event" и текст "This is an updated test event".
    response = client.put(
        '/api/v1/calendar/1/',
        data="2024-01-22|Updated Event|This is an updated test event")
    # Проверяем, что код ответа равен 200, что означает успешное обновление ресурса.
    assert response.status_code == 200
    # Проверяем, что в данных ответа содержится строка "update", указывающая на успешное обновление события.
    assert b"update" in response.data


def test_delete_event(client, init_database):
    # Тест на удаление события.
    # Отправляется DELETE-запрос для удаления события с ID 1.
    response = client.delete('/api/v1/calendar/1/')
    # Проверяем, что код ответа равен 200, что означает успешное удаление ресурса.
    assert response.status_code == 200
    # Проверяем, что в данных ответа содержится строка "delete", указывающая на успешное удаление события.
    assert b"delete" in response.data


def test_create_event_title_too_long(client, init_database):
    # Тест на создание события с слишком длинным заголовком (более 30 символов).
    long_title = "A" * 31  # Создаем строку длиной 31 символ (превышение лимита в 30 символов).
    # Отправляется POST-запрос с заголовком, превышающим лимит, и валидным текстом.
    response = client.post(
        '/api/v1/calendar/',
        data=f"2024-01-23|{long_title}|Valid text")
    # Проверяем, что код ответа равен 404, что указывает на ошибку из-за превышения лимита заголовка.
    assert response.status_code == 404
    # Проверяем, что в ответе содержится сообщение "Title length > MAX", указывающее на ошибку валидации заголовка.
    assert b"Title length > MAX" in response.data


def test_create_event_text_too_long(client, init_database):
    # Тест на создание события с слишком длинным текстом (более 200 символов).
    long_text = "B" * 201  # Создаем строку длиной 201 символ (превышение лимита в 200 символов).
    # Отправляется POST-запрос с валидным заголовком и текстом, превышающим лимит.
    response = client.post(
        '/api/v1/calendar/',
        data=f"2024-01-23|Valid title|{long_text}"
        )
    # Проверяем, что код ответа равен 404, что указывает на ошибку из-за превышения лимита текста.
    assert response.status_code == 404
    # Проверяем, что в ответе содержится сообщение "Text length > MAX", указывающее на ошибку валидации текста.
    assert b"Text length > MAX" in response.data


def test_create_duplicate_event_same_day(client, init_database):
    # Тест на создание двух событий в один и тот же день (нельзя добавлять больше одного события в день).
    # Отправляется POST-запрос для создания первого события на дату 2024-01-24.
    response = client.post(
        '/api/v1/calendar/',
        data="2024-01-24|First Event|This is the first event")
    # Проверяем, что код ответа равен 201, что означает успешное создание первого события.
    assert response.status_code == 201
    assert b"new id:" in response.data

    # Отправляется POST-запрос для создания второго события на ту же дату (2024-01-24), что должно вызвать ошибку.
    response = client.post(
        '/api/v1/calendar/',
        data="2024-01-24|Second Event|This is the second event")
    # Проверяем, что код ответа равен 404, что указывает на ошибку из-за попытки создания второго события в тот же день.
    assert response.status_code == 404
    # Проверяем, что в ответе содержится сообщение "Another event already exists on the date", указывающее на ошибку уникальности даты.
    assert b"Another event already exists on the date" in response.data
