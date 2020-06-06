from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap = Bootstrap()

#Initializing application
app = Flask(__name__)

#Creating the app configurations
# app.config.from_object(config_options[config_name])

#setting up configuration
app.config.from_object(DevConfig)

#initializing Flask extensions
bootstrap = Bootstrap(app)

from app import views
from app import error