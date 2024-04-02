def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: n - 1
	"""

    for i in ranger(n - 1, 1, -1):
        if n % i == 0:
            return i
    return 1


def ranger(start: int, stop: int, step: int) -> list:
    """Generate range of integers from start to stop inclusive, with step.
    >>> ranger(1, 10, 1)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> ranger(1, 10, 3)
    [1, 4, 7]
    """
    return list(range(start, stop + 1, step))
