from flask import Flask
from config import Config
from routes import todo_bp
from auth import jwt

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa JWT
jwt.init_app(app)

# Registra as rotas
app.register_blueprint(todo_bp)

if __name__ == "__main__":
    app.run(debug=True)
