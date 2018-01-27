import os
import logging

config = {
    "development": "facebook_robot.config.DevelopmentConfig",
    "testing": "facebook_robot.config.TestingConfig",
    "default": "facebook_robot.config.DevelopmentConfig"
}

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # dialect+driver://username:password@host:port/database
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'postgresql://botapi:botapi@127.0.0.1:5432/botapi'
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'bookshelf.log'
    LOGGING_LEVEL = logging.DEBUG

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://botapi:botapi@127.0.0.1:5432/botapi'
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://botapi:botapi@127.0.0.1:5432/botapi'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    print('Start profile config : ' , config_name)
    app.config.from_object(config[config_name]) # object-based default configuration
    #app.config.from_pyfile('config.cfg', silent=True) # instance-folders configuration

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)