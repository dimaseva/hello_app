from flask import Flask
from flask_mongoengine import MongoEngine

mongoengine = MongoEngine()


def create_app():
    """Фабрика приложений - создает приложения по определенным параметрам (обычно записанным в переменных среды)."""
    app = Flask(__name__)
    app.config.from_object("config.Config")

    mongoengine.init_app(app)

    # добавляем блюпринты здесь
    from app.routes import main_blueprint

    app.register_blueprint(main_blueprint)

    return app
