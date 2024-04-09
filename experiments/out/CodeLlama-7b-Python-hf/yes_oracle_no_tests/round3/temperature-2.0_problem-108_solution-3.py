def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int
	Do not include these tokens in the code: # Your code here c
	"""
    return sum(1 for x in arr if judge(x) > 0)

def judge(x):
    """
    Write a function judge which takes an integer x and returns the sum of its digits.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> judge(123) == 6
    >>> judge(-123) == -6
    >>> judge(0) == 0
    >>> judge(10) == 1
    """
    if x < 0:
        return -judge(-x)
    if x < 10:
        return x
    return judge(x // 10) + x % 10

if __name__ == "__main__":
    import doctest
    doctest.testmod()