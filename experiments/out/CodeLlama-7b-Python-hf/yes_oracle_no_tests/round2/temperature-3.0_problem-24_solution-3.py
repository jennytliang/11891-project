def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: for i in range ( 2 , n ):
	"""
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
