"""" creating app """

from flask import Flask
from instance.config import app_config
from app.api.v1 import views

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.register_blueprint(views.BASE_URL_BP)
    
    return app


