def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: l
	Do not include these tokens in the code: list
	"""

    so_far = []
    for x in l:
        so_far.append(x)
        so_far.sort()
        if len(so_far) % 2 == 0:
            return (so_far[len(so_far) // 2 - 1] + so_far[len(so_far) // 2]) / 2
        else:
            return so_far[len(so_far) // 2]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
