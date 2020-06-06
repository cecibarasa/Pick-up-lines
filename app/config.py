import os
class Config:
    '''
    general parent class
    '''

    pass

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