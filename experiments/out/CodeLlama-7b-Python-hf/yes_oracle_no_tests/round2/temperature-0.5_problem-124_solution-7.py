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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert valid_date('03-11-2000') == True, "1st example"
    assert valid_date('15-01-2012') == False, "2nd example"
    assert valid_date('04-0-2040') == False, "3rd example"
    assert valid_date('06-04-2020') == True, "4th example"
    assert valid_date('06/04/2020') == False, "5th example"
    assert valid_date('13-04-2020') == True, "6th example"
    assert valid_date('01-01-1999') == True, "7th example"
    assert valid_date('13-04-2019') == True, "8th example"
    assert valid_date('04-06-1999') == False, "9th example"
    assert valid_date('13-04-1999') == False, "10th example"
    assert valid_date('13-04-2019') == True, "11th example"
    assert valid_date('13-04-2021') == False, "12th example"
    assert valid_date('13-04-2018') == True, "13th example"
    assert valid_date('13-13-2018') == False, "14th example"
    assert valid_date('13-01-2018') == False, "15th example"
    assert valid_date('13-04-2017') == False, "16th example"
    assert valid_date('13-04-2022') == False, "17th example"
    assert valid_date('05-