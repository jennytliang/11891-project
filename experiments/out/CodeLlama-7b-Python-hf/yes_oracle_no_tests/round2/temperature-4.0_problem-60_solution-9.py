def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)


def sum_to_n2(n: int):
    """sum_to_n2 is a function that sums numbers from 1 to n.
    >>> sum_to_n2(30)
    465
    >>> sum_to_n2(100)
    5050
    >>> sum_to_n2(5)
    15
    >>> sum_to_n2(10)
    55
    >>> sum_to_n2(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    if n == 1:
        return 1
    return n + sum_to_n2(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
