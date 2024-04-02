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
    is_valid_date = True
				
	
    #######################################
    #code below (which is mine) starts here#
    #######################################
    date_list = list(date.split('-'))
    if len(date) == 0 or len(date_list) != 3:
        is_valid_date = False
    else:
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
        if not (month > 0 and month <= 12):
            is_valid_date = False
        elif day == 0:
            is_valid_date = False
        elif year < 0 or year >= 2050:
            is_valid_date = False
        elif year < 1900:
            is_valid_date = False
        elif year > 2049:
            is_valid_date = False
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or 
             month == 10 or month == 12 and day < 1 or day > 31:
            is_valid_date = False
        elif month == 2 and day < 1 or day > 28:
            is_valid_date = False
        elif month == 4 or month == 6 or month == 9 or month == 11 and day < 1 
             or day > 30:
            is_valid_date = False
        elif year % 4 == 0 and day > 29:
            is_valid_date = False
        elif year % 100 == 0 and day > 29:
            is_valid_date = False
        elif year % 400 == 0 and day > 29:
            is_valid_date = False
        else:
            is_valid_date = True
    return is_valid_date
    #######################################
		 #code by me ends here#
    #######################################
