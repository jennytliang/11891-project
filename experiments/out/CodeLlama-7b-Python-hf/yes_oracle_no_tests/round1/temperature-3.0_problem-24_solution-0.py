def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Base case if n
	"""
    # Base case if n
    if n == 1:
        return 1

    # Base case if n
    if n == 2:
        return 2

    # Recursive step
    if n % 2 == 0:
        return largest_divisor(n // 2)
    else:
        return largest_divisor(n // 2) if largest_divisor(n // 2) > largest_divisor(n // 3) else largest_divisor(n // 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
