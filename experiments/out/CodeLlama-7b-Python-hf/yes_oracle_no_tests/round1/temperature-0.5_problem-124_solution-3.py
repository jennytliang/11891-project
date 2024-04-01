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
    
	Include these tokens in the code:  days = [ 3 1 ,  2
	"""

    month_days = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30, 2: 28, 2: 29}
    try:
        mm, dd, yyyy = date.split('-')
        mm, dd, yyyy = int(mm), int(dd), int(yyyy)
        if mm in month_days.keys() and dd in range(1, month_days[mm] + 1) and yyyy > 0:
            return True
    except:
        pass
    return False


assert valid_date('03-11-2000') == True
assert valid_date('15-01-2012') == False
assert valid_date('04-0-2040') == False
assert valid_date('06-04-2020') == True
assert valid_date('06/04/2020') == False
