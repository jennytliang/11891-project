def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""
    pass

def sum_digits(x):
    """
    Write a function sum_digits which takes an integer and returns the sum of its digits.
    >>> sum_digits(10)
    1
    >>> sum_digits(42)
    6
    >>> sum_digits(420)
    6
    >>> sum_digits(123)
    6
    >>> sum_digits(-456)
    7
    """
    pass

def count_positive_nums(arr):
    """
    Write a function count_positive_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_positive_nums([]) == 0
    >>> count_positive_nums([-1, 11, -11]) == 1
    >>> count_positive_nums([1, 1, 2]) == 3
    >>> count_positive_nums([1, 1, -2]) == 2
    >>> count_positive_nums([1, -1, -2]) == 1
    """
    pass

def count_nums_with_even_sum(arr):
    """
    Write a function count_nums_with_even_sum which takes an array of integers and returns
    the number of elements which has a sum of digits even.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums_with_even_sum([]) == 0
    >>> count_nums_with_even_sum([-1, 11, -11]) == 0
    >>> count_nums_with_even_sum([1, 1, 2]) == 1
    >>> count_nums_with_even_sum([