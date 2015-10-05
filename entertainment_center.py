# imports
import fresh_tomatoes
import media


# insertion of the titles, resume, image and trailer of my avorites
# movies using the class Movie from the file media
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy who play \
                        together",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


star_wars_4 = media.Movie("Star Wars: Episode IV - A New Hope",
                          "Luke Skywalker to the rescue, or?",
                          "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # noqa
                          "https://www.youtube.com/watch?v=hb8kJ7F-_1s")  # noqa


star_wars_6 = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                           "Destruction of the Death Star",
                           "http://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",  # noqa
                           "www.youtube.com/watch?v=5UfA_aKBGMc")


star_wars_5 = media.Movie("Star Wars: Episode V - Empire Strikes Back",
                          "The bumpy road to Jedi mastery",
                          "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # noqa
                          "www.youtube.com/watch?v=PkEKIw0FU6Y")


gattaca = media.Movie("Gattaca",
                      "A genetically inferior man assumes the identity\
                      of a superior one in order to pursue his lifelon\
                      g dream of space travel",
                      "http://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",  # noqa
                      "www.youtube.com/watch?v=ZppWok6SX88")


# set all my new favorites movies in an array
movies = [toy_story, avatar, star_wars_4, star_wars_5, star_wars_6,
          gattaca]

# launch the function open_movies_page with the list of my favorites
# movies in it
fresh_tomatoes.open_movies_page(movies)
