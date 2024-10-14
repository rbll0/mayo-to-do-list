from flask import Flask
from flask_jwt_extended import JWTManager
from redis import Redis
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, template_folder='../templates')  # Garantindo que ele busca a pasta correta de templates
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    cache = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], db=app.config['REDIS_DB'])

    with app.app_context():
        from app import routes

    return app
