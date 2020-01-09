import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ENV = 'development'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'user.db')

class ProductionConfig(Config):
    ENV = 'production'
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)