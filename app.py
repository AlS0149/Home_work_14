from flask import Flask

from utils import get_movie_by_title, get_movie_by_year, get_movie_by_rating, get_movie_by_genre

app = Flask(__name__)


@app.route("/movie/<title>")
def page_movies(title):
    get_title = get_movie_by_title(title)

    return get_title


@app.route("/movie/<year_from>/to/<year_to>")
def page_years(year_from, year_to):
    get_year = get_movie_by_year(year_from, year_to)

    return get_year


@app.route("/movie/rating/<rating>")
def page_rating(rating):
    get_rating = get_movie_by_rating(rating)

    return get_rating


@app.route("/movie/genre/<genre>")
def page_genre(genre):
    get_genre = get_movie_by_genre(genre)

    return get_genre


if __name__ == '__main__':
    app.run()
