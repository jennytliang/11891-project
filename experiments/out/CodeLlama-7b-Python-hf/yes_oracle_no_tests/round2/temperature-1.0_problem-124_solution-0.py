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
	Do not include these tokens in the code: from datetime import datetime date
	"""
    day, month, year = input("Please enter the date in the dd-mm-yyyy format : ").split("-") 

    if len(year)+len(month)+len(day) != 10:
        return False
    try : 
        int(day)
        int(month)
        int(year)
    except :
        return False
    months = [1, 3, 5, 7, 8, 10, 12]
    feb = [4, 6, 9, 11]
    if int(month) in months:
        if int(day) < 1 or int(day) > 31:
            return False
    if int(month) in feb:
        if int(day) < 1 or int(day) > 28:
            return False
    if int(month) == 2:
        if int(day) < 1 or int(day) > 29:
            return False
    return True
    
# keep this function call here  
# to see how to enter arguments in Python scroll to line 17
print(valid_date("09-14-2017"))
print(valid_date("15-01-2012"))
print(valid_date("10-01-2012"))
print(valid_date("29-02-2100"))
print(valid_date("29-02-1xxx"))
print(valid_date("06/04/2020"))
