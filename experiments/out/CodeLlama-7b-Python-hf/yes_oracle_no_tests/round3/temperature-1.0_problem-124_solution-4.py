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
    
	Include these tokens in the code: 9
	Do not include these tokens in the code: 8
	"""


    days = 0
    months = 0
    years = 0

    # Split the date string into three parts using "-" as the delimiter
    parts = date.split("-")

    # Check if the length of the parts array is 3
    if len(parts) == 3:
        # Convert the string parts into integers
        months = int(parts[0])
        days = int(parts[1])
        years = int(parts[2])
    else:
        return False

    # Check for valid year
    if years < 1 or years > 9999:
        return False

    # Check for valid month
    if months < 1 or months > 12:
        return False

    # Check for valid day
    if months == 2:
        # Check for valid day in February
        if days < 1 or days > 29:
            return False
    elif months in [1,3,5,7,8,10,12]:
        # Check for valid day in months 1,3,5,7,8,10,12
        if days < 1 or days > 31:
            return False
    elif months in [4,6,9,11]:
        # Check for valid day in months 4,6,9,11
        if days < 1 or days > 30:
            return False
    else:
        # If the month is any other month, the day must be between 1 and 31
        if days < 1 or days > 31:
            return False

    return True


print(valid_date("03-11-2000")) # True
print(valid_date("15-01-2012")) # False
print(valid_date("04-0-2040")) # False
print(valid_date("06-04-2020")) # True
print(valid_date("06/04/2020")) # False
