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

    # Write your code here
    if date == "" or " ":
        return False

    data = date.split("-")
    if len(data) != 3:  
        return False

    month, day, year = data

    if month == "" or " ":
        return False
    if day == "" or " ":
        return False
    if year == "" or " ":
        return False

    if int(year) < 2001:
        return False

    months = ["1","3","5","7","8","10","12", "4","6","9","12","1","4","6","9","11"]
    if not int(month) in months:
        return False

    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    i = months.index(month) 
    d=days[i]

    if int(d) < 1 or int(day) < 1 :
        return False
    else:
        if int(day) > int(d):
            return False

    return True
        
    
    
    
        
    
    














    
    
print(valid_date('04-0-2020'))