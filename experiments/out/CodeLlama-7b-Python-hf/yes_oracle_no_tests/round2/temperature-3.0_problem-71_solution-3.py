def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    
	Do not include these tokens in the code: # your code here
	'''
    if a + b > c and a + c > b and b + c > a:
        return (a+b+c)/2 * ((a+b+c)/2 - a)**0.5
    else:
        return -1

print(triangle_area(3, 4, 5))
# 6.00
print(triangle_area(1, 2, 10))
# -1


def is_leap_year(year):
    '''
    Given a year, return True if the year is a leap year, and False otherwise.
    
    A year is a leap year if it is divisible by 4, except it is not a leap
    year if it is divisible by 100, unless the year is also divisible by 400.
    
    Example:
    is_leap_year(1990) == False
    is_leap_year(2000) == True
    is_leap_year(2004) == True
    
	Do not include these tokens in the code: # your code here
	'''
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(1990))
# False
print(is_leap_year(2000))
# True
print(is_leap_year(2004))
# True


def sum_digits(number):
    '''
    Given an integer, return the sum of its digits.
    
    Example:
    sum_digits(4321) == 10
    sum_digits(42) == 6
    sum_digits(420) == 6
    
	Do not include these tokens in the code: # your code here
	'''
    return sum([int(i) for i in str(number)])

print(sum_digits(4321))
# 1