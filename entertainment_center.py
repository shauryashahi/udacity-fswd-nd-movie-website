import media
import fresh_tomatoes

# Toy Story : movie title, storyline, poster image and movie trailer 
toy_story = media.Movie(
  "Toy Story",
  "A story about a boy and his toys that come to life",
  "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # NOQA
  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Shawshank Redemption : movie title, storyline, poster image and movie trailer
shawshank = media.Movie(
  "Shawshank Redemption",
  "A story about a man who escapes prison after years of hardship.",
  "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",  # NOQA
  "https://www.youtube.com/watch?v=6hB3S9bIaco")

# Pulp Fiction : movie title, storyline, poster image and movie trailer
pulp_fiction = media.Movie(
  "Pulp Fiction",
  "A gangster comedy movie.",
  "https://s-media-cache-ak0.pinimg.com/236x/6b/cc/f8/6bccf86a2590a9ad883f47219096e136.jpg",  # NOQA
  "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Godfather : movie title, storyline, poster image and movie trailer
godfather = media.Movie(
  "Godfather",
  "A story about a criminal family.",
  "https://www.cinematerial.com/media/posters/md/1s/1suyyfwy.jpg",  # NOQA
  "https://www.youtube.com/watch?v=sY1S34973zA")

# Goodfellas : movie title, storyline, poster image and movie trailer
goodfellas = media.Movie(
  "Goodfellas",
  "A story about a bunch of gangsters.",
  "http://www.impawards.com/1990/posters/goodfellas_xlg.jpg",  # NOQA
  "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

# Harry Potter : movie title, storyline, poster image and movie trailer
harry_potter = media.Movie(
  "Harry Potter",
  "A story about a boy wizard who fights his enemy Lord Voldemort",
  "http://img.moviepostershop.com/harry-potter-and-the-deathly-hallows-part-ii-movie-poster-2011-1010709870.jpg",  # NOQA
  "https://www.youtube.com/watch?v=_EC2tmFVNNE")


movies = [
  toy_story,
  shawshank,
  pulp_fiction,
  godfather,
  goodfellas,
  harry_potter
  ]
fresh_tomatoes.open_movies_page(movies)
