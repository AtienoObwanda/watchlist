from flask import render_template
from app import app
from .request import get_movies, get_movie

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
    #message='Hello Moringa'
    # return render_template('demo.html', message=message)
   

@app.route('/movie/<int:id>')
# @app.route('/movie/<movie_id>')

# def movie(movie_id):
def movie(id):
    '''
    View movie page function that returns index page and it's data'
    '''
    # title = f'Currently viewing {movie_id}'
    # return render_template('movie.html', title=title)

    movie = get_movie(id)
    title = f'{movie.title}'
    # reviews = Review.get_reviews(movie.id)

    return render_template('movie.html',title = title,movie = movie) #reviews = reviews