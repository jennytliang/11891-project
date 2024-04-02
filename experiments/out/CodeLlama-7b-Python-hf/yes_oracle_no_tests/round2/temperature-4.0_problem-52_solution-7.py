def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: print ( below _ th reshold ([ 1 ,
	"""


    return all(x < t for x i l)

if __name__ == '__main__':
    import doctest
    doctest.testmod()