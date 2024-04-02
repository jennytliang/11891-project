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

    # write your code here
    import datetime
    import re
    import calendar
    if len(date) == 0:
        return False
    else:
        date = date.split('-')
        if int(date[0]) < 1 or int(date[0]) > 12:
            return False
        if int(date[0]) == 4 or int(date[0]) == 6 or int(date[0]) == 9 or int(date[0]) == 11:
            if int(date[1]) < 1 or int(date[1]) > 30:
                return False
        elif int(date[0]) == 1 or int(date[0]) == 3 or int(date[0]) == 5 or int(date[0]) == 7 or int(date[0]) == 8 or int(date[0]) == 10 or int(date[0]) == 12:
            if int(date[1]) < 1 or int(date[1]) > 31:
                return False
        else:
            if int(date[1]) < 1 or int(date[1]) > 29:
                return False
        if int(date[2]) < 0 or int(date[2]) > 9999:
            return False
        return True


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
