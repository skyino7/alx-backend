#!/usr/bin/env python3
"""Parametrize templates"""

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


def get_user():
    """Get user"""
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None

def before_request():
    """Before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Get locale"""
    user = g.user('user', None)
    if user:
        locale = user.get('locale')
        if locale in app.config["LANGUAGES"]:
            return user['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Index page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
