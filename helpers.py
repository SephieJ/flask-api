# -*- coding: utf-8 -*-

from dateutil.parser import *
from datetime import datetime


def convert_date(date):
    date = (parse(str(date)))
    parsed_date = datetime.strftime(date, '%Y-%m-%d')
    return parsed_date


# def date_parser(date_from):
# 	date = parse(str(date_from))


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
