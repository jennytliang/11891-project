def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    
	Include these tokens in the code: list
	Do not include these tokens in the code: 0 def get _ negative
	"""


    
    positive = []
    for num in l:
        if num > 0:
            positive.append(num)
    return positive





if __name__ == "__main__":
    import doctest
    doctest.testmod()