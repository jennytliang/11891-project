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


def valid_date_time(date_time):
    """You have to write a function which validates a given date time string
    and returns True if the date time is valid otherwise False.
    The date time is valid if all of the following rules are satisfied:
    1. The date time string is not empty.
    2. The date should be in the format: mm-dd-yyyy hh:mm:ss
    3. The number of hours should be between 0 and 23.
    4. The number of minutes should be between 0 and 59.
    5. The number of seconds should be between 0 and 59.
    6. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    7. The months should not be less than 1 or higher than 12.
    8. The date time should be in the format: mm-dd-yyyy hh:mm:ss

    for example: 
    valid_date_time('03-11-2000 01:05:10') => True

    valid_date_time('15-01-2012 13:05:10') => False

    valid_date_time('04-0-2040 22:05:10') => False

    valid_date_time('06-04-2020 12:05:10') => True

    valid_date_time('06/04/2020 23:05:10') => False
    
	Include these tokens in the code: days = [ 3 1 ,
	"""
    pass


def valid_time(time):
    """You have to write a function which validates a given