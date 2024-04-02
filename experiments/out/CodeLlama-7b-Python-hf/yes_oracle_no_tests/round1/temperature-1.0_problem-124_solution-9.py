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
	days = (3, 1, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30)
	months = (1,2,3,4,5,6,7,8,9,10,11,12)

    date = date.replace(".","")
    date = date.replace("/", "")

    datearr = date.split("-")[::-1]
    
    if len(datearr) != 3:
        return False
    
    try:
        month = int(datearr[0])
        day = int(datearr[1])
        year = int(datearr[2])
    except ValueError:
        return False
    
    if month < 1 or month > 12 or day < 0 or day > 31:
        return False
    
    if month in months and day < 1 or day > days[month-1]:
        return False
    
    if month in (4, 6, 9, 11) and day < 1 or day > 30:
        return False
    
    if month ==  2 and day >29:
        return False
    
    return True
    pass