# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS


# Configuration
DEBUG = True


# Instantiate the extract
extract = Flask(__name__)
extract.config.from_object(__name__)
CORS(extract)

folder = 'templates/'


@extract.route('/')
def index_page():
    return 'Hello'


if __name__ == '__main__':
    extract.run(host="localhost", port=5001, threaded=True, debug=True)
