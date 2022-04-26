class Movie:
    '''
    Movie class to define Movie object
    '''

    def __init__(self, id, title,overview, poster,vote_average, vote_count):
       
        self.id = id
        self.title = title
        self.overview = overview
        self.poster =  poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        