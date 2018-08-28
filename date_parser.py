# -*- coding: utf-8 -*-

from datetime import datetime, date
from dateutil import relativedelta
import re
import calendar

user_input = input('Get date:')
text = user_input.lower()
text = text.replace(" ", "")
month_day_list = ['january', 'february',
                  'march', 'april', 'may', 'june', 'july',
                  'august', 'september', 'october', 'november', 'december',
                  'monday', 'tuesday', 'wednesday', 'thursday',
                  'friday', 'saturday', 'sunday']
result = ''.join(user_input)
result = re.sub('st|of|th|to', '', result)
result.replace(" ", "")


if text == 'lastweek':
    date = date.today() - relativedelta.relativedelta(days=7)
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
if text == 'nextweek':
    date = date.today() + relativedelta.relativedelta(days=7)
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
if text == "lastmonth":
    date = date.today() - relativedelta.relativedelta(months=1)
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
if text == "nextmonth":
    date = date.today() + relativedelta.relativedelta(months=1)
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
if text == "yesterday":
    date = date.today() - relativedelta.relativedelta(days=1)
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
if text == "tomorrow":
    date = date.today() + relativedelta.relativedelta(days=1)
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
if text == "today":
    date = date.today()
    date = datetime.strftime(date, '%m-%d-%Y')
    print(date)
