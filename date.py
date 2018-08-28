# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
from dateutil import relativedelta
import re
import calendar
import sys

# date_to = datetime.now()
# parse = datetime.strftime(date_to, '%m-%d-%Y')
# day = date.today()
user_input = input('Get date:')
text = user_input.lower()
month_list = ['january', 'february',
              'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']
# month_day_list = ''.join(month_day_list)
day_num = re.findall(r'\d+', user_input)
check_input = re.findall(r'\w+', text)
result = ''.join(text).replace(" ", "")

datem = datetime.today().strftime("%Y")
# today = datetime.today().strftime("%m-%d-" + datem)
try:
    if "to" in check_input:
        check_input.remove('to')
        result = [re.sub('st|nd|rd|th|of', '', x).title() for x in check_input]
        data = list(filter(None, result))
        data1 = datetime.strptime(
            data[0], '%B').strftime('%m-01-' + datem)
        data2 = datetime.strptime(
            data[1], '%B').strftime('%m-01-' + datem)
        date_result = data1 + ' to ' + data2
        if data1 <= data2:
            print(date_result)
        else:
            print("Date range exceeded!")
    else:
        if result in month_list:
            data = datetime.strptime(
                result, '%B').strftime('%m-01-' + datem)
            print(data)
        else:
            print('No date found!')
except ValueError:
    print('No date found!')


# if 'last' in check_input:
#     lastDay = date.today()
#     oneday = relativedelta.relativedelta(days=1)
#     if check_input[1] == 'monday':
#         while lastDay.weekday() != calendar.MONDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'tuesday':
#         while lastDay.weekday() != calendar.TUESDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'wednesday':
#         while lastDay.weekday() != calendar.WEDNESDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'thursday':
#         while lastDay.weekday() != calendar.THURSDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'friday':
#         while lastDay.weekday() != calendar.FRIDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'saturday':
#         while lastDay.weekday() != calendar.SATURDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'sunday':
#         while lastDay.weekday() != calendar.SUNDAY:
#             lastDay -= oneday
#         print(lastDay.strftime('%m-%d-%Y'))
#     else:
#         print('No date found!')
# elif 'next' in check_input:
#     nextDay = date.today()
#     oneday = relativedelta.relativedelta(days=1)
#     if check_input[1] == 'monday':
#         while nextDay.weekday() != calendar.MONDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'tuesday':
#         while nextDay.weekday() != calendar.TUESDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'wednesday':
#         while nextDay.weekday() != calendar.WEDNESDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'thursday':
#         while nextDay.weekday() != calendar.THURSDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'friday':
#         while nextDay.weekday() != calendar.FRIDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'saturday':
#         while nextDay.weekday() != calendar.SATURDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     elif check_input[1] == 'sunday':
#         while nextDay.weekday() != calendar.SUNDAY:
#             nextDay += oneday
#         print(nextDay.strftime('%m-%d-%Y'))
#     else:
#         print('No date found!')
# else:
#     print('No date found!')

# if check_input[1] in month_day_list:
#     print(check_input[1])
#     today = date.today()
#     last_day = today - relativedelta.relativedelta(days=7)
#     date = datetime.strftime(last_day, '%m-%d-%Y')
#     print(date)

# if "of" in result:
#     result = re.sub('st|nd|rd|of|th', '', result)
#     result.replace(" ", "")
#     result = datetime.strptime(
#         result, '%d%B').strftime('%m-%d-' + datem)
#     print(result)
# elif result == 'lastweek':
#     date = date.today() - relativedelta.relativedelta(days=7)
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# elif result == 'nextweek':
#     date = date.today() + relativedelta.relativedelta(days=7)
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# elif result == "lastmonth":
#     date = date.today() - relativedelta.relativedelta(months=1)
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# elif result == "nextmonth":
#     date = date.today() + relativedelta.relativedelta(months=1)
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# elif result == "yesterday":
#     date = date.today() - relativedelta.relativedelta(days=1)
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# elif result == "tomorrow":
#     date = date.today() + relativedelta.relativedelta(days=1)
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# elif result == "today":
#     date = date.today()
#     date = datetime.strftime(date, '%m-%d-%Y')
#     print(date)
# else:
#     result = re.sub('st|nd|rd|th', '', result)
#     result.replace(" ", "")
#     result = datetime.strptime(
#         result, '%B%d').strftime(
#         '%m-%d-2018')
#     print(result)


# print(day)

# print(result)

# print({'month': month_list}, {'day': day_list})
"""
2.b July to December
2.c July
2.i next monday
2.j last monday
"""
