from flask import Flask
from flask_json import FlaskJSON
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from views.auth import auth_blueprint
from views.user import user_blueprint
from config import Config
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    json = FlaskJSON(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(user_blueprint, url_prefix="/user")


app = create_app()
