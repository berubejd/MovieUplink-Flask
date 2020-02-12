from flask import Blueprint, current_app as app, redirect, render_template, url_for

from . import create_app

movie_count = 5


main_bp = Blueprint(
    "routes", __name__, template_folder="templates", static_folder="static"
)


@main_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main_bp.route("/top-rated", methods=["GET"])
def top_rated():
    response = app.client.top_rated()
    return render_template(
        "display.html",
        page_type="Top Rated Movies",
        movie_url=app.movie_url,
        genres = app.genres,
        movies=response[:movie_count],
    )


@main_bp.route("/now-playing", methods=["GET"])
def now_playing():
    response = app.client.now_playing()
    return render_template(
        "display.html",
        page_type="Now Playing",
        movie_url=app.movie_url,
        genres = app.genres,
        movies=response[:movie_count],
    )


@main_bp.route("/trending", methods=["GET"])
def trending():
    response = app.client.now_trending()
    return render_template(
        "display.html",
        page_type="Trending Movies",
        movie_url=app.movie_url,
        genres = app.genres,
        movies=response[:movie_count],
    )
