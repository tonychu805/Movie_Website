import webbrowser

class Movie():

    def __init__(self,movie_title,storyline,poster_link,youtube_link):
        self.title = movie_title
        self.story = storyline
        self.poster_image_url = poster_link
        self.trailer_youtube_url = youtube_link

    #instance Method to show movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    #instance Method to show movie's poster
    def show_poster(self):
        webbrowser.open(self.poster_image_url)

