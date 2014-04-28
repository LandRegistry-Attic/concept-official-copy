#!/usr/bin/env python

from flask import Flask, render_template
import os
import json
import logging

app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Logging
@app.before_first_request
def setup_logging():
    if not app.debug:
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

@app.route('/')
def home():
    return 'Land Registry'

if __name__ == '__main__':
    app.run()
