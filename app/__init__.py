"""" creating app """

from flask import Flask
from instance.config import app_config
from app.api.v1 import party_views, office_views

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.register_blueprint(party_views.BASE_URL_BP)
    app.register_blueprint(office_views.BASE_URL_BP)
    app.register_blueprint(party_views.HOME_PAGE)
    
    return app


