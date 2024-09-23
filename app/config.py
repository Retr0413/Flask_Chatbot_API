import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'youe_secret_key')
    MYSQL_HOS = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'your_username')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'your_password')
    MYSQL_DB = os.getenv('MYSQL_DB', 'chatbot_db')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))

config = Config()