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
	Do not include these tokens in the code: if date . count (' - ')
	"""
    import re
    
    if not date:
        return False
    d,m,y = date.split('-')
    m,d,y = map ( int , [m,d,y])
    if d >31 or d <1:
        return False
    elif m%2:
        if d >30 or d <1:
            return False
    elif not m%2:
        if d >31 or d <1:
            return False
    elif m >12 or m <1:
        return False
    elif not bool ( re . search ( r'\d{2}-\d{2}-\d{4}' , date ) ) or not len (date) == 10:
        return False
    
    return True
    
    
print(valid_date('03-11-2000')) #True
print(valid_date('15-01-2012')) #False
print(valid_date('04-0-2040')) #False
print(valid_date('06-04-2020')) #True
print(valid_date('06/04/2020')) #False
    
