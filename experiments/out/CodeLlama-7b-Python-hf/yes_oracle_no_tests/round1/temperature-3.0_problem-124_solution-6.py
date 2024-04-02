def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    
	Include these tokens in the code: days = [ 3 1 ,
	"""
    pass


def valid_time(time):
    """You have to write a function which validates a given time string and
    returns True if the time is valid otherwise False.
    The time is valid if all of the following rules are satisfied:
    1. The time string is not empty.
    2. The hours should not be less than 0 or higher than 23.
    3. The minutes should not be less than 0 or higher than 59.
    4. The seconds should not be less than 0 or higher than 59.
    5. The time should be in the format: hh-mm-ss

    for example: 
    valid_time('09:20:30') => True

    valid_time('19:55:59') => True

    valid_time('25:23:12') => False

    valid_time('02:60:29') => False

    valid_time('12-31-2020') => False
    
	Include these tokens in the code: hours = [ 2 1 ,
	"""
    pass


def valid_datetime(datetime):
    """You have to write a function which validates a given date time string and
    returns True if the date time is valid otherwise False.
    The date time is valid if all of the following rules are satisfied:
    1. The date time string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The hours should not be less than 0 or higher than 23.
    5. The minutes should not be less than 0 or higher than 59.
    6. The seconds should not