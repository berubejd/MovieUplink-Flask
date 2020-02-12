import os
import pathlib
import requests
import requests_cache
import sys

from datetime import timedelta
from uplink import Consumer, get, response_handler, returns, Path
from uplink.auth import ApiTokenParam

from flask import current_app as app


api_key = app.config["API_KEY"]
cache_file = app.config["CACHEDB_NAME"]

expire_after = timedelta(hours=4)
requests_cache.install_cache(cache_name=str(cache_file), expire_after=expire_after)
requests_cache.remove_expired_responses()


@response_handler
def actually_return_json_results(response):
    """ This is necessary because @returns.json doesn't work for whatever reason """
    return response.json()["results"]


@response_handler
def raise_for_status(response):
    """ Check for issues returned by target web server and exit if needed """
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit()

    return response


token_auth = ApiTokenParam("api_key", api_key)


@raise_for_status
class MovieClient(Consumer):
    def __init__(
        self,
        base_url="https://api.themoviedb.org/3/",
        client=None,
        converters=(),
        auth=token_auth,
        hooks=(),
        **kwargs
    ):
        super().__init__(
            base_url=base_url,
            client=client,
            converters=converters,
            auth=auth,
            hooks=hooks,
            **kwargs
        )

    @get("configuration")
    def configuration(self) -> requests.models.Response:
        """ Retrieve the current TMDb configuration information """

    @get("genre/movie/list")
    def genres(self) -> requests.models.Response:
        """ Retrieve list of available movie genres """

    @actually_return_json_results
    @get("movie/now_playing?language=en-US&page=1&region=US")
    def now_playing(self) -> requests.models.Response:
        """ Retrieve list of movies currently in theatres """

    @actually_return_json_results
    @get("trending/movie/day")
    def now_trending(self) -> requests.models.Response:
        """ Retrieve list of movies trending in the last 24 hours """

    @actually_return_json_results
    @get("movie/top_rated?language=en-US&page=1&region=US")
    def top_rated(self) -> requests.models.Response:
        """ Retrieve the top rated movies according to users of TMDb """


def process_genres(client) -> dict:
    """ Request genre id = name mapping for use in movie details later """
    genres = client.genres()

    return {genre["id"]: genre["name"] for genre in genres.json()["genres"]}
