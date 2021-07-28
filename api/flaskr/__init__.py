# import os

from flask import Flask
from flask_cors import CORS # This fixes the error in React app regarding the CORS policy

from . import home
from . import show


def create_app(test_config=None):
    # create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='',
        static_folder='../../build',
        template_folder='../../build'
    )
    CORS(app)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    app.register_blueprint(home.bp)
    app.register_blueprint(show.bp)

    return app