import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story about a boy and his toys that come to life","http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
shawshank = media.Movie("Shawshank Redemption","A story about a boy and his toys that come to life","http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")
pulp_fiction = media.Movie("Pulp Fiction","A story about a boy and his toys that come to life","https://s-media-cache-ak0.pinimg.com/236x/6b/cc/f8/6bccf86a2590a9ad883f47219096e136.jpg","https://www.youtube.com/watch?v=s7EdQ4FqbhY")
godfather  = media.Movie("Godfather","A story about a boy and his toys that come to life","https://www.cinematerial.com/media/posters/md/1s/1suyyfwy.jpg","https://www.youtube.com/watch?v=sY1S34973zA")
goodfellas = media.Movie("Goodfellas","A story about a boy and his toys that come to life","http://www.impawards.com/1990/posters/goodfellas_xlg.jpg","https://www.youtube.com/watch?v=qo5jJpHtI1Y")
harry_potter = media.Movie("Harry Potter","A story about a boy and his toys that come to life","http://img.moviepostershop.com/harry-potter-and-the-deathly-hallows-part-ii-movie-poster-2011-1010709870.jpg","https://www.youtube.com/watch?v=_EC2tmFVNNE")


movies = [toy_story,shawshank,pulp_fiction,godfather,goodfellas,harry_potter]
fresh_tomatoes.open_movies_page(movies)
