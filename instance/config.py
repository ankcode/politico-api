import os

class Config():
    DEBUG = False
    SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfing(Config):
    TESTING = True
    DEBUG = True

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfing
}