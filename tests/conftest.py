import pytest
# from server import app as flask_app
from server import app as flask_app
from app.db import CalendarDB

@pytest.fixture(scope='module')
def app():
    # Настройка приложения для тестирования
    flask_app.config['TESTING'] = True
    yield flask_app


@pytest.fixture(scope='module')
def client(app):
    # Создание тестового клиента
    return app.test_client()


@pytest.fixture(scope='module')
def init_database():
    # Инициализация базы данных перед тестами
    db = CalendarDB()
    # Здесь можно добавить код для создания тестовых данных
    yield db
    # Здесь можно добавить код для очистки базы данных после тестов
    db.clear()
