# Movie Uplink - Flask

This Flask app is an update to my [MovieUplink](https://github.com/berubejd/MovieUplink) console application from December 2019.  It incorporates the API calls made by that application, which used [Uplink](https://uplink.readthedocs.io/en/stable/index.html) to model the API while also retaining the [request caching](https://github.com/reclosedev/requests-cache) I was originally using.

I kicked off this Flask project using the [Flask-Starter](https://github.com/berubejd/Flask-Starter) project I built previously.

## Screenshots

![Movie Uplink Flask Screenshot](images/movieuplink-flask.png?raw-true)

![Movie Uplink Flask Movie Detail Screenshot](images/movieuplink-flask-detail.png?raw-true)

## Configuration
This application requires an API key which should be stored in the environment with a small number of other values.  The necessary key can be generated on the [The Movie Database API portal](https://developers.themoviedb.org/3/getting-started/introduction).
