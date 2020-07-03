from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
#We import the Blueprint class from flask.
#  We then initialize the Blueprint class by creating a variable main. 
# The Blueprint class takes in 2 arguments.
#  The name of the blueprint and the __name__ variable to find the location of the blueprint.

# def create_app(config_name):
#     app Flask(__name__)


#     #Creating the app configurations 
#     app.config.from_object(config_options[config_name])

#     #Initializing flask extensions
#     bootstrap.init_app(app)

#     #Registiring the blueprint
#     from .main import main as main blueprint
#     app.register_blueprint(main_blueprint)

#     return app