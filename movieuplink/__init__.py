from flask import Flask, g, render_template


def not_found(e):
    return render_template("error.html"), 404


def create_app(test_config=None):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        app.config.from_object("config.Config")

    else:
        app.config.from_object("config.TestingConfig")

    # Register Error Handlers
    app.register_error_handler(404, not_found)

    # Register Blueprints
    from . import routes

    app.register_blueprint(routes.main_bp)
    app.add_url_rule("/", endpoint="index")

    with app.app_context():
        # Import API
        from . import api

        print("Creating movie client.")
        app.client = api.MovieClient()
        app.genres = api.process_genres(app.client)

        config = app.client.configuration().json()
        
        if config:
            base_url = config["images"]["secure_base_url"]
            size = "w1280" if "w1280" in config["images"]["backdrop_sizes"] else "original"

            app.movie_url = base_url + size
    
    return app
