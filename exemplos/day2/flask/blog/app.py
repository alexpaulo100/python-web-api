from blog.config import configure
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    configure(app)
    return app
