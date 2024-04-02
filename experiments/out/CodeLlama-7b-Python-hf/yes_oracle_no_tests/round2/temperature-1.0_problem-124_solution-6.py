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
    
	Do not include these tokens in the code: if "/ " in date or "-
	"""


    return (not "/" in date) and (date != "") and (year_date(date) or year_date(date)[0] and year_date(date)[1])

def month_len(year):
 
    y = year % 4
    f = [1908,1904,1900,1896,1892,1888,1884,1880]
    c = [1900,1800,1900,1800,1900,1800]
    if year < min(f) and year % 4 > 0: return 28
    elif year < min(c) and year % 100 > 0: return 29
    elif year < min(f) and year % 100 == 0 or year in f: return 29
    else: return 28
 
 
def year_date(date):
    """ check year """
 
    month,day,year = map(int,date.split("-"))    
    if day > month_len(year): return False
    elif month not in range(1,13): return False
    elif not day in range(1,month_len(year)+1): return False
    else: return True
