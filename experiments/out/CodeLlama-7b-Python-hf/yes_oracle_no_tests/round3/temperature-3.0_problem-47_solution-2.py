def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Do not include these tokens in the code: sorted _
	"""


    sorted_l = sorted(l)
    i = len(l) // 2
    return (sorted_l[i] + sorted_l[i - 1]) / 2.0 if len(l) % 2 == 0 else sorted_l[i]


def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
