def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: (
	"""

    retur = True
    for num in l:
        if num >= t:
            retur = False
            break
    return retur


if __name__ == "__main__":
    import doctest
    doctest.testmod()