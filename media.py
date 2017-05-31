import webbrowser

''' This class makes up a movie object with basic movie details.'''
class Movie():

  ''' inputs movie title, storyline, poster image, trailer video url'''
  def __init__(self, title, storyline, poster_image, trailer_youtube):
    self.title = title
    self.storyline = storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
    

  ''' This function opens up a youtube video in a new browser window.'''
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)

