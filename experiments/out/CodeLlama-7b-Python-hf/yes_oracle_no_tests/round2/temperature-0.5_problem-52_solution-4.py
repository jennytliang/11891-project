def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: x
	Do not include these tokens in the code: n
	"""


    retur = True
    for x in l:
        if x > t:
            retur = False
            break
    return retur


