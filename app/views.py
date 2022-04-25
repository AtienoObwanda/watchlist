from flask import render_template
from app import app

#Views
@app.route('/')
def index():

    '''
    View root page function that returns index page and it's data
    '''

    message = 'Hello Mish'
    return render_template('index.html', message=message)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns index page and it's data'
    '''
    return render_template('movie.html',id=movie_id)