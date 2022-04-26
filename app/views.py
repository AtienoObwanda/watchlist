from flask import render_template
from app import app
from .request import get_movies

#Views
@app.route('/')
def index():

    '''
    View root page function that returns index page and it's data
    '''
     #gettin popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    #title
    title = 'Home - Welcome to The best Movie Review Website!'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

   

@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns index page and it's data'
    '''
    title = f'Currently viewing {movie_id}'
    return render_template('movie.html', title=title)

