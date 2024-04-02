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
    split_date = date.split("-")
    if len(split_date) != 3:
        return False

    month, day, year = split_date

    if month not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        return False

    if day.isdigit() is False:
        return False

    if month == "02":
        if day.isdigit() is False:
            return False
        
        if len(day) != 2:
            return False
        
        if int(day) > 29:
            return False
        
        if year % 4 == 0:
            if int(day) > 29:
                return False
        
        if int(day) < 1:
            return False
    else:
        if int(day) > 31:
            return False
        
        if int(day) < 1:
            return False

        if month in ["01", "03", "05", "07", "08", "10", "12"]:
            return True

        if month in ["04", "06", "09", "11"]:
            return True
        








def main():
    pass


if __name__ == "__main__":
    main()