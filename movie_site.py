import media
import fresh_tomatoes

#Original Entries
toy_story = media.Movie("Tony Story",
                        "A story of toys",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )
avatar = media.Movie("Avatar",
                     "An outerspace utopia",
                     "https://s-media-cache-ak0.pinimg.com/736x/f7/bc/7b/f7bc7b19e7f8555ba0f36aa3f2bc5dcd.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )

inception = media.Movie("Inception",
                        "Dream within dreams",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0"
                        )

zootopia = media.Movie("Zootopia",
                       "Advanced animal kingdom",
                       "http://cdn.collider.com/wp-content/uploads/2015/12/zootopia-movie-poster.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM"
                       )

deadpool = media.Movie("Deadpool",
                       "Mutant mercenary",
                       "http://cdn.traileraddict.com/content/20th-century-fox/deadpool-poster-8.jpg",
                       "https://www.youtube.com/watch?v=ZIM1HydF9UA"
                       )

armageddon = media.Movie("Armageddon",
                         "Apocalyptic event",
                         "http://vignette3.wikia.nocookie.net/voiceacting/images/d/de/Armageddon_1998_Poster.jpg/revision/latest?cb=20130627171145",
                         "https://www.youtube.com/watch?v=iq6q2BrTino"
                         )

movie_list = [toy_story, avatar, inception, zootopia, deadpool, armageddon]


#Allow users to Update the movie list by themselves
def update_movie_list():
    
    movie_title = raw_input("Please Enter Movie Title. Please enter None if there's no new movie: " )

    while movie_title != "None":
        story = raw_input("Please Enter Synopsis: ")
        poster_link = raw_input("Please enter poster url: ")
        youtube_trailer=raw_input("Please enter trailer youtube link: ")
        movie = media.Movie(movie_title,story,poster_link,youtube_trailer)
        movie_list.append(movie)
        movie_title = raw_input("Please Enter Movie Title. Please enter None if finished: " )
            
         
    return movie_list

#Open the website of the list of your favorite movies
def open_movie_database():
    fresh_tomatoes.open_movies_page(movie_list)

#Delete the movie that you no longer want in the database
def remove_movie_list(movie_list):
    
    if movie_list == []:
        print "No movie available"
    else:
        for movie in movie_list:
            print movie.title
            
        remove_entry(movie_list)                       
            
        return movie_list
    
#Allow users to delete        
def remove_entry():

    movie_to_be_deleted = raw_input("\nEnter the title of the movie that you wish to remove from the database: ")

    for movie in movie_list:
        if movie.title == movie_to_be_deleted:
            movie_list.remove(movie)
            print "The movie has been deleted"
            break 

open_movie_database()

'''    
avatar.show_trailer()

open_movie_database()

update_movie_list()

open_movie_database()

remove_entry()

open_movie_database()
'''
