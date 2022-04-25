from flask import Config


class config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child class

    Args: 

        Config the parent configuration class with general configuration settings
    '''
    
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:

        Config the parent configuration class with General configuration settings

    '''
   
    DEBUG=True