import webbrowser


class Movie:
    """ This class provides a way to store movie related information and show trailer
    Attributes:
        title (str): This saves title of movie.
        poster_image_url (str): This saves a url linking to poster image of movie.
        trailer_youtube_url (str): This saves a url linking to trailer of movie.
    Method:
        __init__()    : This init a instance of class Movie.
        show_trailer(): This helps to show trailer of movie.
    """


    def __init__(self, movie_title, post_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = post_image
        self.trailer_youtube_url =  trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
