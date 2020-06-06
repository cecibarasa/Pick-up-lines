class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nabalayo:kartie@localhost/project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class ProdConfig:
    '''
    production config child class
    '''
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig:
    '''
    development config class
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}