import webbrowser


class Movie():
    #Introduction about class Movie
    """ This class porivdes a way to store movie related information
    Attributes:
        title (str): This saves title of movie.
        poster_image_url (str): This saves a url linking to poster image of movie.
        trailer_youtube_url (str): This saves a url linking to trailer of movie.
    Method:
        show_trailer(): this helps to show trailer of movie.
        
    """


    # Init a insance of class Movie
    def __init__(self, movie_title, post_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = post_image
        self.trailer_youtube_url =  trailer_youtube


    #Open web browser and show trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
                                                                                
