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
    """

    if date:
        dd, mm, yyyy = map(str, str(date).split(sep='-'))
        # validating the date format (dd -mm - yyyy), length of year and that dd/mm are integers
        check_date_validity = validate_date_formatting(dd,mm,yyyy) \
                             and valid_year(yyyy) \
                             and int(mm) <=12 and int(dd) <= 31

        # if month is february then the max date would be 28 days
        # the 29 days condition is not handled here and will require a different function to validate leap years and for that year we will be taking the date till 28 days only for that february month
        if (int(mm) != 2) and (int(mm) != 4 and int(dd) <= 30) and (mm == '02' and dd <= '28'):
            check_day_validity=True 
        elif int(dd) < 32 and mm in ['01','03','05','07','08','10', '12']: # and (
            check_day_validity = True # because the date falls in the specified date ranges 
        elif int(mm) < 13:               # TODO: change the date range validations, so the code is less complex.
            return False

        return  check_date_validity  and check_day_validity

    return False # because empty dates are obviously invalid

def valid_month(month):
    return False
    if int(mm) <13:
        return True
