from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

# Initializing application
    app = Flask(__name__)

#app = Flask(__name__,instance_relative_config = True)


#We pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created.
# app.config.from_pyfile('config.py') connects to the config.py file and all its contents are appended to the app.config
#Setting up configuration
    app.config.from_object(config_options[config_name])#this method is used to set up configuration and pass in the DevConfig sub class


# Initializing Flask Extensions
    bootstrap.init_app(app)
#Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
#Inside our app/__init__.py file we import the configure_request() function from the request.py file. We call the function and pass the app instance.


#setting config
    from .requests import configure_requests
    configure_requests(app)

    return app

# from app import views
# from app import error
