#!/usr/bin/env python3
"""0-app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config = Config


@app.route("/")
def hello_world():
    """hello_world function"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
