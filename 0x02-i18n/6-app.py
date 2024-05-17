#!/usr/bin/env python3
"""
Change your get_locale function
to use a user’s preferred local
if it is supported.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Get user"""
    login_as = request.args.get('login_as')
    if login_as is not None and int(login_as) in users:
        return users[int(login_as)]
    return None


@app.before_request
def before_request() -> None:
    """Before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Index page"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
