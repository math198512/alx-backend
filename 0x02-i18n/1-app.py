#!/usr/bin/env python3
"""Basic Flask app"""
import babel
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """template that simply outputs Welcome to Holberton"""
    return render_template('1-index.html')
