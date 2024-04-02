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
    
	Include these tokens in the code: days
	"""
    
    if date == "" or len(date) != 10:
        return False
    else: 
        days = 0
        for idx in range(0,10,3):
            # first digit is month
            if int(date[idx]) >= 0 and int(date[idx]) <= 12:
                if int(date[idx]) != 2: days = days + 31
                elif int(date[idx]) == 2: days = days + 28
                else: days = days + 30 # rest are fine

            # remaining two digits are date
            if int(date[idx+1] + date[idx+2]) >= 0 and int(date[idx+1] + date[idx+2]) <= 31: days = days + int(date[idx+1] + date[idx+2])

            # third digit is year
            if int(date[idx+3]) > 1899: return False
            else: return True