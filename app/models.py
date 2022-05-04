from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Movie:
    '''
    Movie class to define Movie object
    '''

    def __init__(self, id, title,overview, poster,vote_average, vote_count):
       
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count





class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        
    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    @property #to create a write only class property password. 
    def password(self):
        raise AttributeError('You cannot read the password attribute') #to block access to the password property. 

    @password.setter #set this property we generate a password hash and pass the hashed password as a value to the pass_secure column property to save to the database.
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password): # takes in a password, hashes it and compares it to the hashed password to check if they are the same.
        return check_password_hash(self.pass_secure, password)


    def __repr__(self):
        return f'User {self.username}'





class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'