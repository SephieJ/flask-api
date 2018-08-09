# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import os
import glob


# Configuration
DEBUG = True


# Instantiate the extract
extract = Flask(__name__)
extract.config.from_object(__name__)
CORS(extract)


@extract.route('/')
def index_page():
    folder = 'temp_aiml/'
    for filename in glob.glob(os.path.join(folder, '*.aiml')):
        print(filename)
        with open(filename, 'r') as myfile:
            soup = BeautifulSoup(myfile.read(), 'html.parser')
        data = []
        for cat in soup.find_all('category'):
            if cat.parent.name == "topic":
                continue
            data += [cat.find("pattern").text]
        print(data)
        data_set = " ".join(data)
        return data_set


if __name__ == '__main__':
    extract.run(host="localhost", port=5001, threaded=True, debug=True)
