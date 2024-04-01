def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""


  # Write your code here.

    odd = lambda x: x % 2 != 0
    def check_digits(num):
        if num // 10 % 2 != 0 and num % 10 % 2 != 0:
            return True
        else:
            return False

    return len([num for num in nums if num > 10 and check_digits(num)])



# tests

def test_specialFilter_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_3():
    assert specialFilter([5, 7, 9, 11, 12, 13, 14]) == 0

def test_specialFilter_4():
    assert specialFilter([]) == 0

def test_specialFilter_5():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_specialFilter_6():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 0

def test_specialFilter_7():
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 0

def test_specialFilter_8():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 23,