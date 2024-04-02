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
    import re

    regex = r"^([0-1]?[0-9]|2[0-9])\-(0?[1-9]|1[0-2])\-([0-9]{4})$"
    match = re.match(regex, date)
    if not match:
        return False
    else:
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))

        if 0 < day <= 31:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day >= 1 and day <= 31:
                    return True
                else:
                    return False
            elif month in [4, 6, 9, 11]:
                if day >= 1 and day <= 30:
                    return True
                else:
                    return False
            elif month == 2:
                if day >= 1 and day <= 29:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


def test_valid_date():
    assert valid_date("03-11-2000") == True
    assert valid_date("15-01-2012") == False
    assert valid_date("04-0-2040") == False
    assert valid_date("06-04-2020") == True
    assert valid_date("06/04/2020") == False


test_valid_date()
