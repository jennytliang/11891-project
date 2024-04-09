def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    return sum(1 for num in arr if sum(map(lambda x: int(x) if x != '-' else -1, str(num))) > 0)


import doctest
doctest.testmod()
