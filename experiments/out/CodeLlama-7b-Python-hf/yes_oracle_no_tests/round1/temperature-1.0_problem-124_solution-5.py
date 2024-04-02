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
    if date.count('-') != 2:
        return False
    
    month, day, year = date.split('-')

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        valid_days_for_month = (1 <= int(day) <= 31 )
      
    elif int(month) in [4, 6, 9, 11]:
        valid_days_for_month = (1 <= int(day) <= 30 )
    
    else:
        valid_days_for_month = (1 <= int(day) <= 29 )
    
    is_not_empty = len(date) != 0
    is_not_less_or_high_for_month = 1 <= int(month) <= 12
    is_not_less_or_high_for_day = valid_days_for_month
    date_in_right_format = (len(month)==2) and (len(day)==2) and (len(year)==4)
    
    return is_not_empty and is_not_less_or_high_for_month and is_not_less_or_high_for_day and date_in_right_format
    
#     return all([month in '01' or month in '03' or month in '05' or month in '07' or month in '08' or month in '10' or month in '12', int(day) in range(1, 32),
#                year in range(0,2031),
#                '-' .*2 '-'. *4,
#                int(month) in range(1,13),
#                int(day) in range(1,32),
#                int(year[-2:]) in range(10,100)
