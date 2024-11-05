#!/usr/bin/env python3
"""Basic Flask app"""
import babel
from flask import Flask, render_template
from flask_babel import Babel



app = Flask(__name__)
babel = Babel(app)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """template that simply outputs Welcome to Holberton"""
    return render_template('1-index.html')
