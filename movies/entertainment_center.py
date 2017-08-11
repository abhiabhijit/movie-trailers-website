import media
import fresh_tomatoes
import search_trailer

toy_story = media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar=media.Movie("AVATAR",
                   "A MARINE ON AN ALIEN PLANET",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
ironman2=media.Movie("IRON MAN 2",
                     "MARVEL SUPERHERO'S LIFE STORY ",
                     "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                     "https://www.youtube.com/watch?v=R8WwWujC-04")
AVENGERS=media.Movie("AVENGERS",
                                   "SUPERHEROES SAVES THE EARTH FROM EVIL",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                                   "https://www.youtube.com/watch?v=1hPpG4s3-O4")
XMEN=media.Movie("X-Men: Apocalypse",
                               "MUTANT SUPERHEROES",
                               "https://upload.wikimedia.org/wikipedia/en/3/30/X-Men_Legends_II_-_Rise_of_Apocalypse_Coverart.png",
                               "https://www.youtube.com/watch?v=COvnHv42T-A")
THEMUMMYRETURNS=media.Movie("THE MUMMY 3",
                            "STORY OF EGYPTIAN MUMMY ",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
                            "https://www.youtube.com/watch?v=IjHgzkQM2Sg")

movies = [toy_story,avatar,ironman2,AVENGERS,XMEN,THEMUMMYRETURNS]

fresh_tomatoes.open_movies_page(movies)  
