import media
import fresh_tomatoes
import search_trailer


toy_story = media.Movie("Toy Story",
                      
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v="+search_trailer.search("Toy Story Trailer")
                      )
#print(toy_story.storyline)

avatar=media.Movie("AVATAR",
                       
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "http://www.youtube.com/watch?v="+search_trailer.search("AVATAR Trailer")
                   )
#print(avatar.storyline)
#avatar.show_trailer()
ironman2=media.Movie("IRON MAN 2",
                     
                     "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                     "http://www.youtube.com/watch?v="+search_trailer.search("IRON MAN 2 Trailer")
                     )
AVENGERS=media.Movie("AVENGERS",
                                   
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                     "http://www.youtube.com/watch?v="+search_trailer.search("AVENGERS Trailer")
                                   )
XMEN=media.Movie("X-Men: Apocalypse",
                               "MUTANT SUPERHEROES",
                               "https://upload.wikimedia.org/wikipedia/en/3/30/X-Men_Legends_II_-_Rise_of_Apocalypse_Coverart.png",
                 "http://www.youtube.com/watch?v="+search_trailer.search("X-Men: Apocalypse Trailer")
                              )
THEMUMMY3=media.Movie("THE MUMMY 3 2017",
                           
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
                      "http://www.youtube.com/watch?v="+search_trailer.search("THE MUMMY 3 2017 Trailer")
                           )

movies = [toy_story,avatar,ironman2,AVENGERS,XMEN,THEMUMMY3]

fresh_tomatoes.open_movies_page(movies)  
