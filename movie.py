import webbrowser


class Movie():
    """This class provides a way to store movie related information"""    

    #class variable for movie ratings  
    VALID_RATINGS = ["G", "PG","PG-13", "R"]

    #constructor method for the Movie class, creates objects that are an instance
    #of the Movie class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #instance method, that opens browser window for a given movie object
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    
