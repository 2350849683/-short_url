from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    db.init_app(app)
    from app.service import service
    app.register_blueprint(service)
    return app
