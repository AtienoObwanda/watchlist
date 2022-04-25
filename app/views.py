from flask import render_template
from app import app

#Views
@app.route('/')
def index():

    '''
    View root page function that returns index page and it's data
    '''


    title = 'Home - Welcome to The best Movie Review Website!'
    return render_template('index.html', title=title)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns index page and it's data'
    '''
    title = f'Currently viewing {movie_id}!'
    return render_template('movie.html', title=title)