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
    # split the date string into a list of tokens
    date_tokens = date.split('-')
    if len(date_tokens) != 3:
        return False
    try:
        month = int(date_tokens[0])
        day = int(date_tokens[1])
        year = int(date_tokens[2])
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2:
        if day > 29:
            return False
    if month in [4, 6, 9, 11]:
        if day > 30:
            return False
    return True






