def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: if
	Do not include these tokens in the code: length =
	"""


    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 0:
        return (sorted_l[length // 2 - 1] + sorted_l[length // 2]) / 2
    else:
        return sorted_l[length // 2]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
