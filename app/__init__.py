from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создаем экземпляры SQLAlchemy и Migrate
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """
    Функция для создания и конфигурации Flask приложения.
    """
    app = Flask(__name__)

    # Загрузка конфигурации приложения
    app.config.from_object('config.Config')

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация маршрутов
    with app.app_context():
        from . import routes, models
        db.create_all()  # Создание таблиц в базе данных (если их еще нет)

        # Регистрация маршрутов
        routes.setup_routes(app)

    return app
