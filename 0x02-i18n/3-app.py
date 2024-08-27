#!/usr/bin/env python3
"""3-app Module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config Class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get_locale fucntion"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """hello_world function"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
