def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Base case if n
	"""
    if n % 2 == 0:
        return n // 2
    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
