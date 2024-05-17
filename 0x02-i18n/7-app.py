#!/usr/bin/env python3
"""
Define a get_timezone function
and use the babel.timezoneselector
decorator.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from datetime import datetime
import pytz


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


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone"""
    try:
        timezone = request.args.get("timezone")
        if timezone:
            return pytz.timezone(timezone).zone
        if g.user and g.user.get("timezone"):
            return pytz.timezone(g.user.get("timezone")).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"


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
    current_time = format_datetime(datetime.now())
    return render_template("7-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
