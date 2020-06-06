import os
class Config:
    '''
    general parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nabalayo:karitie@localhost/picklines'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig:
    '''
    production config child class
    '''

    pass

class DevConfig:
    '''
    development config class
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}