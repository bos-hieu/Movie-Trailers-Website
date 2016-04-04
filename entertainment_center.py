import media
import fresh_tomatoes


#take the instances of class Movie about my favorite movies
toy_story = media.Movie("Toy Story",
                        "http:/upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtube.com/watch?v=vwyZH85NQC4")

titanic = media.Movie("Titanic",
                      "https://goo.gl/dTOKw8",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

harry_potter = media.Movie("Harry Potter",
                           "https://goo.gl/9RAQ0H",
                           "https://www.youtube.com/watch?v=JYLdTuL9Wjw")

furious = media.Movie("Furious 7",
                      "https://goo.gl/7k4ZvR",
                      "https://www.youtube.com/watch?v=Skpu5HaVkOc")

arrow = media.Movie("Arrow",
                    "http://goo.gl/egzJkR",
                    "https://www.youtube.com/watch?v=ViFb0paKdgg")

three_Idiots = media.Movie("3 Idiots",
                           "https://goo.gl/W0css6",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w")

#list name of my favorite movies
movies = [toy_story, titanic, harry_potter, furious, arrow, three_Idiots]

#open Movies Trailer page
fresh_tomatoes.open_movies_page(movies)
