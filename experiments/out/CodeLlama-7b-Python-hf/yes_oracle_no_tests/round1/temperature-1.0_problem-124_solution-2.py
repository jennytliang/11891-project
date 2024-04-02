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
    year_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    data = date.split("-")

    try:
        data[1] = int(data[1])
        data[0] = int(data[0])
        data[2] = int(data[2])
        
        if data[0] == 0 or data[1] == 0 or data[2] == 0:
            return False
        
        if data[1] in [1,3,5,7,8,10,12] and \
                data[1] not in range(1,32):
            return False
        elif data[1] in [4,6,9,11] and \
                data[1] not in range(1,31):
            return False
        elif data[1] == 2 and \
                data[1] not in range(1,29):
            return False
          
        if data[0] not in range(1,13):
            return False
            
        if data[2] not in range(0,2022):
            return False
            
        if len(data[0]) != 2 or \
                len(data[1]) != 2 or \
                len(data[2]) != 4:
            return False
            
        return True
    
    except Exception as e:
        print(e)
        return False
         
        
        
if __name__ == '__main__':
    print(valid_date('03-11-2000'))
    print(valid_date('15-01-2012'))
    print(valid_date('04-0-2040'))
    print(valid_date('06-04-2020'))
   