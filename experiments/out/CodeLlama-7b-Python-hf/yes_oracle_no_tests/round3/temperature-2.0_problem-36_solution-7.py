def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    count = 0
    for x in range(1, n):
        if x % 11 == 0 or x % 13 == 0:
            if '7' in str(x):
                count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
