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

    # your code goes here
    import re
    import datetime
    import calendar
    if date == '':
        return False
    else:
        # split the date into three tokens
        date_split = date.split('-')
        # get the number of days
        day = date_split[1]
        # get the number of months
        month = date_split[0]
        # get the number of years
        year = date_split[2]
        # check if the date is valid
        if day < 1 or day > 31:
            return False
        elif month < 1 or month > 12:
            return False
        elif year < 1:
            return False
        else:
            month_days = calendar.monthrange(int(year), int(month))[1]
            if month in [4, 6, 9, 11] and day > 30:
                return False
            elif month == 2 and day > 28:
                return False
            elif month in [1, 3, 5, 7, 8, 10, 12] and day > month_days:
                return False
            else:
                return True


def test_valid_date():
    assert valid_date('03-11-2000') == True
    assert valid_date('15-01-2012') == False
    assert valid_date('04-0-2040') == False
    assert valid_date('06-04-2020') == True
    assert valid_date('06/04/2020') == False
    assert valid_date('12-12-2020') == True
    assert valid_date('12/12/2020') == False
    assert valid_date('12-12-202') == False
    assert valid_date('12-12-20200') == False
    assert valid_date('12-12-20200') == False
    assert valid