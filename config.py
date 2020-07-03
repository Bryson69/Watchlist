import os

class Config:
    '''
    General configuration parent class 
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('f58b5a44d7ac0eae36baf9b86c8e2097')
    SECRET_KEY = os.environ.get('123456')


class ProdConfig(Config):#subclass contains configurations that are used in production stages of our application and inherits from the parent Config class
    '''
    Production configuration parent child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass


class DevConfig(Config):#subclass contains configurations that are used in development stages of our application and inherits from the parent Config class.
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    DEBUG = True #enables debug mode
#We use {} to represent sections in the url that will be replaced with actual values

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}