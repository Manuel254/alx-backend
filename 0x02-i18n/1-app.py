#!/usr/bin/env python3
"""This module contains a basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from pytz import timezone


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Creates a configuration for the app"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index():
    """This is the index route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
