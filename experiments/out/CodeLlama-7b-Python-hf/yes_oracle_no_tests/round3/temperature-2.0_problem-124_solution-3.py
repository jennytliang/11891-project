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
    import re
    import datetime

    def valid_date(date):
        # check for empty string
        if date == "":
            return False

        # check for correct format
        if re.match(r"[0-9]{2}\-[0-9]{2}\-[0-9]{4}", date):
            month, day, year = date.split('-')

            # check for valid month
            if int(month) not in range(1, 13):
                return False

            # check for valid day
            if int(day) not in range(1, 32):
                return False

            # check for valid year
            if int(year) not in range(1900, datetime.datetime.now().year + 1):
                return False

            # check for valid date
            try:
                datetime.datetime(int(year), int(month), int(day))
                return True
            except ValueError:
                return False

        else:
            return False
    return valid_date(date)


print(valid_date("03-11-2000"))  # => True
print(valid_date("15-01-2012"))  # => False
print(valid_date("04-0-2040"))  # => False
print(valid_date("06-04-2020"))  # => True
print(valid_date("06/04/2020"))  # => False