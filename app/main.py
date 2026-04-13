from flask import Flask
from flask_cors import CORS

from app.database import init_db
from app.config import config
from app.views import views


def add_views(app):
    for view in views:
        app.register_blueprint(view)


def configure_app(app, config, overrides):
    for key, value in config.items():
        if key in overrides:
            app.config[key] = overrides[key]
        else:
            app.config[key] = config[key]


def create_app(config_overrides={}):
    app = Flask(__name__, static_url_path='/static')
    configure_app(app, config, config_overrides)
    CORS(app)
    add_views(app)
    init_db(app)
    app.app_context().push()
    return app
