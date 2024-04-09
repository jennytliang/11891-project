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
    
	Do not include these tokens in the code: # Write your code here .
	"""
    import datetime
    from datetime import date
    import re
    # Write your code here
    if len(date) == 0:
        return False
    else:
        date_list = date.split('-')
        date_list[0] = int(date_list[0])
        date_list[1] = int(date_list[1])
        date_list[2] = int(date_list[2])
        
        if date_list[0] in [1,3,5,7,8,10,12] and date_list[1] not in range(1,32):
            return False
        if date_list[0] in [4,6,9,11] and date_list[1] not in range(1,31):
            return False
        if date_list[0] == 2 and date_list[1] not in range(1,29):
            return False
        if date_list[0] not in range(1,13):
            return False
        if len(date_list) != 3:
            return False
        
        if date_list[2] < 1 or date_list[2] > 9999:
            return False
        
        if len(date_list[0]) != 2 or len(date_list[1]) != 2:
            return False
        
        if date_list[0] in [1,3,5,7,8,10,12] and date_list[1] in range(1,32):
            return True
        if date_list[0] in [4,6,9,11] and date_list[1] in range(1,31):
            return True
        if date_list[0] == 2 and date_list[1] in range(1,29):
            return True
        if date_list[0] in range(1,13):
            return True
        
        





























