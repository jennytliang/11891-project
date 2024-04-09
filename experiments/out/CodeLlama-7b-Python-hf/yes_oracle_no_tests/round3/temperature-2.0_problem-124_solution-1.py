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
    # your code here
    # split date
    # check if it's valid
    # check if it's in the format 'mm-dd-yyyy'
    # check if the month is valid
    # check if the day is valid
    # check if the year is valid
    # return True or False
    # date = date.split("-")
    # if date[0] in [1,3,5,7,8,10,12]:
    #     if date[1] < 1 or date[1] > 31:
    #         return False
    # elif date[0] in [4,6,9,11]:
    #     if date[1] < 1 or date[1] > 30:
    #         return False
    # elif date[0] == 2:
    #     if date[1] < 1 or date[1] > 29:
    #         return False
    # if date[0] < 1 or date[0] > 12:
    #     return False
    # if date[2] < 0 or date[2] > 9999:
    #     return False
    # if date[2] % 4 == 0:
    #     if date[0] == 2 and date[1] > 29:
    #         return False
    # elif date[2] % 4 != 0:
    #     if date[0] == 2 and date[1] > 28:
    #         return False
    # return True
    # another way to solve this
    import datetime
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
        return True
    except ValueError:
        return False


def valid_date_2(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1