import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Configuração do Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Chave secreta da aplicação Flask
    DEBUG = True  # Ativar modo de depuração para desenvolvimento

    # Configuração do JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Chave secreta para JWT

    # Configuração do Redis
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')  # Host do Redis
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))  # Porta do Redis
    REDIS_DB = int(os.getenv('REDIS_DB', 0))  # Database do Redis

    # Configuração do Banco de Dados (SQLite)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativar a notificação de modificação de objetos

    # HTTPS
    PREFERRED_URL_SCHEME = 'https'  # Define que a aplicação deve preferir HTTPS
