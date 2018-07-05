from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_all(config_name):
    app = Flask(__name__)
    from config import config
    app.config.from_object(config[config_name])
    db.init_app(app)
    from flask_bootstrap import Bootstrap
    Bootstrap(app)
    from flask_babelex import Babel
    Babel(app)
    login_manager.init_app(app)
    from main.home.nav import nav
    nav.init_app(app)

    ##注册蓝本
    from main.home import nav_blueprint
    app.register_blueprint(nav_blueprint)

    return app
