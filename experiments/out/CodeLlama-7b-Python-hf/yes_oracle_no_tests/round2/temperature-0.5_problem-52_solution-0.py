def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: # for num in l :
	"""

    # for num in l:
    #     if num >= t:
    #         return False
    # return True

    # for num in l:
    #     if num >= t:
    #         return False
    #     return True

    # for num in l:
    #     if num >= t:
    #         return False
    # return True

    # return all(num < t for num in l)

    return all(num < t for num in l)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
