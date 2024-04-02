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
    import datetime
    date = date.split('-')
    month = date[0]
    day = date[1]
    year = date[2]


    if len(month) == 1:
        month = "0"+ month
    if len(day) == 1:
        day = "0"+ day

    
    date2 = datetime.date(int(year), int(month), int(day))
    if date2.day <= 31:
        if (int(month) == 1) or (int(month) == 3) or (int(month) == 5) or (int(month) == 7) or (int(month) == 8) or (int(month) == 10) or (int(month) == 12):
            if (int(day) <= 31) and (int(day) >=1):
                return True
            else:
                return False
        elif (int(month) == 4) or (int(month) == 6) or (int(month) == 9) or (int(month) == 11):
            if (int(day) <=30) and (int(day) >= 1):
                return True
            else:
                return False
        else:
            if (int(day) <=29) and (int(day) >= 1):
                return True
            else:
                return False
                           
    else:
        return False




valid_date('04-05-2016')
