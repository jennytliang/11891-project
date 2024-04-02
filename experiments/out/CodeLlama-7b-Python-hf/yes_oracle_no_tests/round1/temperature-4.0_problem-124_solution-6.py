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
    # your code here
    import re
    import datetime
    date_pattern = r'^([0-1]?[0-9]|2[0-9])-([0-1]?[0-9]|2[0-9])-([0-9]{4})$'
    if re.search(date_pattern, date):
        date_list = date.split('-')
        if int(date_list[1]) < 1 or int(date_list[1]) > 31:
            return False
        if int(date_list[0]) == 2 and int(date_list[1]) > 29:
            return False
        if int(date_list[0]) in [4, 6, 9, 11] and int(date_list[1]) > 30:
            return False
        if int(date_list[0]) > 12:
            return False
        if int(date_list[2]) > datetime.datetime.now().year:
            return False
        return True
    else:
        return False


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))