"""
Calculate the time since you stoped smoking.
"""

from datetime import datetime


def how_many_days(stoping_date):
    current_date = datetime.now()
    return current_date - stoping_date


def parse_date(stoping_date):
    datetime_object = datetime.strptime(stoping_date, '%d-%m-%Y')
    return datetime_object


stoping_date = input("When did you stoped smoking (dd-mm-yyyy)? ")

print(how_many_days(parse_date(stoping_date)))
