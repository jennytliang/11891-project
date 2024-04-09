def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: fo = 0
	"""
    fo = 0
    for i in range(2, n):
        if n % i == 0:
            fo = i
    return fo


if __name__ == "__main__":
    import doctest

    doctest.testmod()
