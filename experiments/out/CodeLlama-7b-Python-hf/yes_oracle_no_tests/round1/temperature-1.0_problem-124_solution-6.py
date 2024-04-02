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
    if "/" in date or "-" not in date or len(date) != 10 or \
            int(date[3:5]) < 1 or int(date[3:5]) > 12 or int(date[0:2]) < 1 or \
                    int(date[0:2]) > 31 or len(date) != 10:
        return False
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if date[2] == ' ' or date[7] == ' ':
        return False
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
    if month == 2:
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            if day > 28:
                return False
        else:
            if day > 29:
                return False
    else:
        if day > days[month - 1]:
            return False
    return True

