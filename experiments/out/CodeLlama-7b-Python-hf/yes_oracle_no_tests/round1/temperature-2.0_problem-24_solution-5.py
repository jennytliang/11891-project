def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: n - 1
	"""

    for i in r(1, n):
        if n % i == 0:
            return i
    return n


def r(start: int, end: int) -> int:
    """ Returns a range from start to end, not including end """
    return list(range(start, end))
