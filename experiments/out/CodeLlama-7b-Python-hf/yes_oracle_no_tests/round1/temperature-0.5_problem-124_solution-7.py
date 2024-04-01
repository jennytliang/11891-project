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

    date_parts = date.split("-")
    if len(date_parts) != 3:
        return False
    if len(date_parts[0]) != 2 or len(date_parts[1]) != 2 or len(date_parts[2]) != 4:
        return False
    if date_parts[0] < "01" or date_parts[0] > "12":
        return False
    if date_parts[0] in ["04", "06", "09", "11"]:
        if date_parts[1] < "01" or date_parts[1] > "30":
            return False
    elif date_parts[0] in ["01", "03", "05", "07", "08", "10", "12"]:
        if date_parts[1] < "01" or date_parts[1] > "31":
            return False
    else:
        if date_parts[1] < "01" or date_parts[1] > "29":
            return False
    if int(date_parts[2]) < 1900 or int(date_parts[2]) > 2020:
        return False
    return True


def valid_date1(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy
