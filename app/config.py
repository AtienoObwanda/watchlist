from flask import Config


class config:
    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    Args:
    '''
    Config the parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    Args:
    '''
    Config the parent configuration class with General configuration settings
    '''
    DEBUG=True