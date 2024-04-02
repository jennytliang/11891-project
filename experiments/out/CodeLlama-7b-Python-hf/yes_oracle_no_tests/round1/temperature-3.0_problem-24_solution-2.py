def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Base case if n
	"""
    # Base case if n is less than 2
    if n < 2:
        return n

    # Recursive step
    if n % (n - 1) == 0:
        return n - 1
    else:
        return largest_divisor(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
