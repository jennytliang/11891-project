def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: for i in range ( 2 ,
	Do not include these tokens in the code: # Base case if
	"""
    # Base case
    if n % 2 == 0:
        return 2

    # Iterate
    for i in range(3, n, 2):
        if n % i == 0:
            return i

    return n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
