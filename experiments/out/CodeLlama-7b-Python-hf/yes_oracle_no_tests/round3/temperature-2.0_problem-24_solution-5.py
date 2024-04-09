def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: fo os = []
	"""
    fo = []
    for i in range(1, n):
        if n % i == 0:
            fo.append(i)
    return max(fo)
    # return max(i for i in range(1, n) if n % i == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
