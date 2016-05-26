import movie
import fresh_tomatoes

'''
below lines of code will be creating Movie objects,that will be used on
trailer site
'''
anchor_man = movie.Movie("Anchorman", "The story of Ron Burgundy",
                        "https://s-media-cache-ak0.pinimg.com/236x/7e/90/53/7e905336d3871817d62a26369f413c11.jpg",
                        "https://www.youtube.com/watch?v=-T3wnP91OnI")

the_departed = movie.Movie("The Departed", "A story of deception",
                     "http://images.moviepostershop.com/the-departed-movie-poster-2006-1010399808.jpg",
                     "https://www.youtube.com/watch?v=auYbpnEwBBg")

dark_knight = movie.Movie("The Dark Knight", "Batman faces off with the Joker",
               "http://www.impawards.com/2008/posters/dark_knight_ver5.jpg",
               "https://www.youtube.com/watch?v=yrJL5JxEYIw")

zoolander = movie.Movie("Zoolander", "A story about a model and his life",
               "http://www.fashiongonerogue.com/wp-content/uploads/2015/05/Zoolander-Movie-Poster-Original.jpg",
               "https://www.youtube.com/watch?v=YtQq0T3ExLs")

dumb_and_dumber = movie.Movie("Dumb and Dumber", "A movie about two very dumb"
                              +" friends",
                                 "http://ecx.images-amazon.com/images/I/51Z07DwVJmL._SY355_.jpg",
                                 "https://www.youtube.com/watch?v=l13yPhimE3o")

jungle_book = movie.Movie("The Jungle Book", "The story of a boy growing up"
                          +" in the jungle",
               "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_(2016).jpg",
               "https://www.youtube.com/watch?v=HcgJRQWxKnw")


#creates of an array of movies objects to pass to the open_movies_page method
movies = [anchor_man, the_departed, dark_knight, zoolander,
          dumb_and_dumber,jungle_book]

#calls open_movies_page method from the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)





