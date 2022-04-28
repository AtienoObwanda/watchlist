from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

#bootstrap
bootstrap = Bootstrap()

def create_app(config_name): # function that takes the configuration setting key as an argument
    app = Flask(__name__)

    # creating the app configuration
    app.config.from_object(config_options[config_name])

    # Initializing flask extension
    bootstrap.init_app(app)

    # we'll add views and the form

    return app