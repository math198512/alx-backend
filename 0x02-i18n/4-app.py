#!/usr/bin/env python3
"""Basic Flask app with locale"""
import babel
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Instantiate the application object
app = Flask(__name__)

# Wrap the application with Babel
babel = Babel(app)


class Config:
    """
    Config class for locale
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """template that simply outputs Welcome to Holberton"""
    return render_template('3-index.html')
