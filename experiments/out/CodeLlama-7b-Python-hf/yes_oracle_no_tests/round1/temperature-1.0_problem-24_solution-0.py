def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: n - 1
	"""

    for i in r(n - 1):
        if n % i == 0:
            return i


def r(n: int) -> int:
    """ Generates numbers from 1 to n
    >>> r(3)
    [1, 2, 3]
    >>> r(1)
    [1]
    """
    return list(range(1, n + 1))
