#!/usr/bin/env python3
"""3-app Module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config Class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.before_request
def before_request():
    """before_request function"""
    setattr(g, "user", get_user(request.args.get("login_as", 0)))


def get_user(user_id) -> Union[Dict[str, Union[str, None]], None]:
    """get_user"""
    return users.get(int(user_id), 0)


@babel.localeselector
def get_locale() -> str:
    """get_locale fucntion"""
    options = [
        request.args.get("locale", "").strip(),
        g.user.get("locale", None) if g.user else None,
        request.accept_languages.best_match(app.config["LANGUAGES"]),
        Config.BABEL_DEFAULT_LOCALE,
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """hello_world function"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
