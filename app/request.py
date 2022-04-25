import json
from app import app
import urllib.request,json 
from .models import movie

Movie= movie.Movie

#Getting the api key
api_key = app.config['MOVIE_API_KEY']

#Getting movie base url 
base_url = app.config["MOVIE_BASE_URL"]

# def get_movies(category):
#     pass