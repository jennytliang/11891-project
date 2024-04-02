def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

  
    # write your code here
    odd = 10
    count = 0
    for i in nums:
        if i > 10 and (i % odd == 1 or i % odd == 3 or i % odd == 5 or i % odd == 7 or i % odd == 9):
            count += 1
    return count


# tests
def testFilter():

    # corner case: empty array
    assert specialFilter([]) == 0

    # corner case: array with only one number
    assert specialFilter([1]) == 0

    # corner case: array with only two numbers
    assert specialFilter([1, 2]) == 0

    # corner case: array with only three numbers
    assert specialFilter([1, 2, 3]) == 0

    # corner case: array with only four numbers
    assert specialFilter([1, 2, 3, 4]) == 0

    # corner case: array with only five numbers
    assert specialFilter([1, 2, 3, 4, 5]) == 0

    # corner case: array with only six numbers
    assert specialFilter([1, 2, 3, 4, 5, 6]) == 0

    # corner case: array with only seven numbers
    assert specialFilter([1, 2, 3, 4, 5, 6, 7]) == 0

    # corner case: array with only eight numbers
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8]) == 0

    # corner case: array with only nine numbers
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

    # corner case: array with only ten numbers
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

    # corner case: array with only eleven numbers
    assert specialFilter([1, 2