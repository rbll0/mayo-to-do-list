from flask import Flask
from flask_jwt_extended import JWTManager
from redis import Redis
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializando as extensões
jwt = JWTManager(app)
db = SQLAlchemy(app)
cache = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], db=app.config['REDIS_DB'])
