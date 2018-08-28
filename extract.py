# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import os
import glob
from datetime import datetime, date, time
import re


# Configuration
DEBUG = True


# Instantiate the extract
extract = Flask(__name__)
extract.config.from_object(__name__)
CORS(extract)


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
    # print(data_set)


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


@extract.route('/date')
def date_page():
    date_to = datetime.now()
    parse = datetime.strftime(date_to, '%B %d, %Y')
    day = date.today()
    print(day.weekday())
    user_input = '8th of jUly'
    user_input = user_input.lower()
    month_list = ['january', 'february',
                  'march', 'april', 'may', 'june', 'july',
                  'august', 'september', 'october', 'november', 'december']
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday']
    result = int(re.search(r'\d+', user_input).group())
    print(result)

    return jsonify({'month': month_list}, {'day': day_list})


"""
2.a 8th of July
2.b July to December
2.c July
2.d July 1st

2.e Last week
2.f next week
2.g today
2.h tomorrow
2.i next monday
2.j last monday
2.k next month
2.l last month
"""


if __name__ == '__main__':
    extract.run(host="localhost", port=5001, threaded=True, debug=True)
