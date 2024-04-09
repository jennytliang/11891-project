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
    # split date
    date_split = date.split("-")
    # get month
    month = int(date_split[0])
    # get day
    day = int(date_split[1])
    # get year
    year = int(date_split[2])
    # days in a month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # check if days are in range
    if day < 1 or day > days_in_month[month-1]:
        return False
    # check if month is in range
    if month < 1 or month > 12:
        return False
    # check if year is a leap year
    if month == 2 and day == 29 and year % 4 != 0:
        return False
    # check if format is mm-dd-yyyy
    if len(date_split) != 3:
        return False
    # check if hyphen is in the correct position
    if date[2] != "-" or date[5] != "-":
        return False
    
    return True


print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
