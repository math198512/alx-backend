#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """template that simply outputs Welcome to Holberton"""
    return render_template('0-index.html')
