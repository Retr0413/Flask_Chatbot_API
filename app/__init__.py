from flask import Flask
from flask_mysqldb import MySQL
from .config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # 設定のロード
    app.config['MYSQL_HOST'] = Config.MYSQL_HOST
    app.config['MYSQL_USER'] = Config.MYSQL_USER
    app.config['MYSQL_PASSWORD'] = Config.MYSQL_PASSWORD
    app.config['MYSQL_DB'] = Config.MYSQL_DB
    app.config['MYSQL_PORT'] = Config.MYSQL_PORT

    try:
        mysql.init_app(app)
    except Exception as e:
        print(f"Error occurred while initializing the database: {e}")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app