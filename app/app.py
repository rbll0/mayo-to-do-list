from flask import Flask
from flask_jwt_extended import JWTManager
from redis import Redis

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)
cache = Redis(host='localhost', port=6379)

from app import routes, auth
