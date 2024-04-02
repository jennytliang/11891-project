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
	from datetime import datetime
	date = date.split("-")
	mm,dd,YYYY = [int(i) for i in date]
	if YYYY > datetime.now().year or YYYY<1000 or YYYY == datetime.now().year: 
		return False
	else:
		if MM in range (1,13):
			if mm == 2: 			
				days = [31,29,31,30,31,30,31,31,30,31,30,31]				
			elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
				days= [31,28,31,30,31,30,31,31,30,31,30,31]				 			
			elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10
				days= [31,28,31,30,31,30,31,31,30,31,30,31]	
			elif dd == 0 or dd< MM or dd>days[mm] or mm<1 or mm >12 or len(date[0]) != MM or len(date[1]) != 2 or YYYY >3000 or YYYY >2100 or len(date[2]) != 4: 
				return False
		elif dd == 0 or dd< MM or dd>31 or mm<1 or mm >12 or len(date[0]) != MM or len(date[1]) != 2 or YYYY >3000 or YYYY >2100 or len(date[2]) != 4: 
			return False
	return True
    
	result = valid_date(date)
    # Write your code here
    