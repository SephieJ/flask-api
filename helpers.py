# -*- coding: utf-8 -*-

from dateutil.parser import *
from datetime import datetime


def convert_date(date):
    date = (parse(str(date)))
    parsed_date = datetime.strftime(date, '%Y-%m-%d')
    return parsed_date
