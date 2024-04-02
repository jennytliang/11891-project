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
	Do not include these tokens in the code: assert >=
	"""
    total = 0
    for i in range(1, n+1):
        total += i
    return total


def sum_to_n_2(n: int):
    """sum_to_n_2 is a function that sums numbers from 1 to n.
    >>> sum_to_n_2(30)
    465
    >>> sum_to_n_2(100)
    5050
    >>> sum_to_n_2(5)
    15
    >>> sum_to_n_2(10)
    55
    >>> sum_to_n_2(1)
    1
    
	Include these tokens in the code: return ( n +
	Do not include these tokens in the code: assert >=
	"""
    return n * (n + 1) / 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
