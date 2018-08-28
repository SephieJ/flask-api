# -*- coding: utf-8 -*-
# from flask import Flask, jsonify
import re
from functools import partial
import calendar
from datetime import timedelta, date, datetime
from dateutil import relativedelta


# Configuration
# DEBUG = True


# # Instantiate the extract
# refactor = Flask(__name__)
# refactor.config.from_object(__name__)


def Cus_Recompile(dic, sentence):
    word_re = re.compile(r'\b[a-zA-Z]+\b')
    return word_re.sub(partial(replace_helper, dic), sentence)


def replace_helper(dic, match):
    word = match.group(0)
    return dic.get(word, word)


def clean_sen(sentence):
    sentence = sentence
    monthabbr = dict((v, k) for v, k in zip(
        calendar.month_name[1:], calendar.month_abbr[1:]))
    dates_type = {
        "last week": date.today() - relativedelta.relativedelta(days=7),
        "last month": date.today() - relativedelta.relativedelta(months=1),
        "last night": date.today() - relativedelta.relativedelta(days=1),
        "last day": date.today() - relativedelta.relativedelta(days=1),

        "next week": date.today() + relativedelta.relativedelta(days=7),
        "next month": date.today() + relativedelta.relativedelta(months=1),
        "next day": date.today() + relativedelta.relativedelta(days=1),
        "next night": date.today() + relativedelta.relativedelta(days=1),

        "today": date.today().strftime('%d-%b-%Y'),
        "tomorrow": date.today() + relativedelta.relativedelta(days=1),
        "yesterday": date.today() - relativedelta.relativedelta(days=1),

        "XXxo of Month": monthabbr,

        "until": "to",

    }
    one_sen_cons = {
        "last night": dates_type['last night'].strftime('%d-%b-%Y'),
        "last day": dates_type['last day'].strftime('%d-%b-%Y'),
        "last week": dates_type['last week'].strftime('%d-%b-%Y'),
        "last month": dates_type['last month'].strftime('%d-%b-%Y'),

        "next night": dates_type['next night'].strftime('%d-%b-%Y'),
        "next day": dates_type['next day'].strftime('%d-%b-%Y'),
        "next week": dates_type['next week'].strftime('%d-%b-%Y'),
        "next month": dates_type['next month'].strftime('%d-%b-%Y'),

        "today": dates_type['today'],
        "tomorrow": dates_type['tomorrow'].strftime('%d-%b-%Y'),
        "yesterday": dates_type['yesterday'].strftime('%d-%b-%Y'),
        "until": 'to'
    }

    return Cus_Recompile(one_sen_cons, sentence.lower())


# one_sen_cons = {
#     "last night": dates_type['last night'].strftime('%d-%b-%Y'),
#     "last day": dates_type['last day'].strftime('%d-%b-%Y'),
#     "last week": dates_type['last week'].strftime('%d-%b-%Y'),
#     "last month": dates_type['last month'].strftime('%d-%b-%Y'),

#     "next night": dates_type['next night'].strftime('%d-%b-%Y'),
#     "next day": dates_type['next day'].strftime('%d-%b-%Y'),
#     "next week": dates_type['next week'].strftime('%d-%b-%Y'),
#     "next month": dates_type['next month'].strftime('%d-%b-%Y'),

#     "today": dates_type['today'],
#     "tomorrow": dates_type['tomorrow'].strftime('%d-%b-%Y'),
#     "yesterday": dates_type['yesterday'].strftime('%d-%b-%Y'),
#     "XXxo of Month": [monthabbr]
# }
sentence = 'next day next day'
print(clean_sen(sentence))


# @refactor.route('/')
# def index_date():
#     monthabbr = dict((v, k) for v, k in zip(
#         calendar.month_name[1:], calendar.month_abbr[1:]))
#     word_re = re.compile(r'\b[a-zA-Z]+\b')
#     x = calendar.day_name[
#         (date.today() - timedelta(days=1)).weekday()]
#     print(x)
#     dates_type = {
#         "last week": date.today() - relativedelta.relativedelta(days=7),
#         "last month": date.today() - relativedelta.relativedelta(months=1),
#         "last day": date.today() - relativedelta.relativedelta(days=1),
#         "last night": date.today() - relativedelta.relativedelta(days=1),

#         "next week": date.today() + relativedelta.relativedelta(days=7),
#         "next month": date.today() + relativedelta.relativedelta(months=1),
#         "next day": date.today() + relativedelta.relativedelta(days=1),
#         "next night": date.today() + relativedelta.relativedelta(days=1),

#         "today": date.today().strftime('%d-%b-%Y'),
#         "tomorrow": date.today() + relativedelta.relativedelta(days=1),
#         "yesterday": date.today() - relativedelta.relativedelta(days=1),

#         "XXxo of Month": list(monthabbr.values()),

#         "until": "to",

#     }
#     one_sen_cons = {
#         "last night": dates_type['last night'].strftime('%d-%b-%Y'),
#         "last day": dates_type['last day'].strftime('%d-%b-%Y'),
#         "last week": dates_type['last week'].strftime('%d-%b-%Y'),
#         "last month": dates_type['last month'].strftime('%d-%b-%Y'),

#         "next night": dates_type['next night'].strftime('%d-%b-%Y'),
#         "next day": dates_type['next day'].strftime('%d-%b-%Y'),
#         "next week": dates_type['next week'].strftime('%d-%b-%Y'),
#         "next month": dates_type['next month'].strftime('%d-%b-%Y'),

#         "today": dates_type['today'],
#         "tomorrow": dates_type['tomorrow'].strftime('%d-%b-%Y'),
#         "yesterday": dates_type['yesterday'].strftime('%d-%b-%Y'),

#         "XXxo of Month": dates_type['XXxo of Month'],
#     }

#     return jsonify(one_sen_cons)


# if __name__ == '__main__':
#     refactor.run(host="localhost", port=5002, threaded=True, debug=True)
