# /app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    mongo.init_app(app)

    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app