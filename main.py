from flask import Flask, render_template
import tmdb_client
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=12)
    return render_template("homepage.html", movies=movies)


# @app.route("/popular/", methods=["GET"])
# def todos_list():
#     movies = tmdb_client.get_popular_movies()
#     return jsonify(movies)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}



@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    how_many2=4
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_cast(movie_id, how_many2)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)