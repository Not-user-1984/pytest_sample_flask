# API Календаря

## Ограничения

Максимальная длина заголовка: 30 символов.

Максимальная длина текста: 200 символов.

Нельзя добавить больше одного события в день.

## API Интерфейс

## Установить библиотеки из файла requerements.txt
```
pip install -r requirements.txt
```
## запуск приложения

```
$ flask --app api.py run
```

## запуск тестов

```
pytest -v
```

## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-22|title|new text"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|title|new text

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-21|title|looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: Text length > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2024-01-21|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
new id: 2

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-21|title|text"
failed to CREATE with: Another event already exists on the date: b'2024-01-21
```
