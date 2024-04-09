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
    # split the date string using '-' to get the list of days, months and years
    # if the length of the list is not equal to 3, then return False
    if len(date.split('-')) != 3:
        return False

    # get the list of days, months and years
    days, months, years = date.split('-')

    # try to convert the days, months and years to integers
    # if any of them is not a valid integer, return False
    try:
        days = int(days)
        months = int(months)
        years = int(years)
    except ValueError:
        return False

    # validate the days
    if not (1 <= days <= 31):
        return False

    # validate the months
    if not (1 <= months <= 12):
        return False

    # validate the years
    if not (1900 <= years <= 2020):
        return False

    # the following months have 31 days
    if months in [1, 3, 5, 7, 8, 10, 12]:
        # if the number of days is not between 1 and 31, return False
        if not (1 <= days <= 31):
            return False

    # the following months have 30 days
    if months in [4, 6, 9, 11]:
        # if the number of days is not between 1 and 30, return False
        if not (1 <= days <= 30):
            return False

    # the month of February has 28 days and 29 days
    if months == 2:
        # if the number of days is not between 1 and 29, return False
        if not (1 <= days <= 29):
            return False

    # if all of the above rules are satisfied, return True
    return True


def test_valid_date():
    assert valid_date('03-11-2000')
    assert not valid_date('15-01-2