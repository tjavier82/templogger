

import os
from flask import Flask


from webapp import routes

def create_webapp(test_config=None):
    # create and configure the app
    webapp = Flask(__name__, instance_relative_config=True)
    webapp.config.from_mapping(
        SECRET_KEY='dev'
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        webapp.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        webapp.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(webapp.instance_path)
    except OSError:
        pass

    return webapp