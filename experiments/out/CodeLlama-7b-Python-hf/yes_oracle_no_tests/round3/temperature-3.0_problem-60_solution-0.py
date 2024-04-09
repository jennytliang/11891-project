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
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


def sum_to_n_alt(n: int):
    """sum_to_n_alt is a function that sums numbers from 1 to n.
    >>> sum_to_n_alt(30)
    465
    >>> sum_to_n_alt(100)
    5050
    >>> sum_to_n_alt(5)
    15
    >>> sum_to_n_alt(10)
    55
    >>> sum_to_n_alt(1)
    1
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_to_n_alt_2(n: int):
    """sum_to_n_alt_2 is a function that sums numbers from 1 to n.
    >>> sum_to_n_alt_2(30)
    465
    >>> sum_to_n_alt_2(100)
    5050
    >>> sum_to_n_alt_2(5)
    15
    >>> sum_to_n_alt_2(10)
    55
    >>> sum_to_n_alt_2(1)
    1
    """
    return sum([i for i in range(1, n + 1)])


def sum_to_n_alt_3(n: int):
    """sum_to_n_alt_3 is a function that sums numbers from 1 to n.
    >>> sum_to_n_alt_3(30)
    465
    >>> sum_to_n_alt_3(100)
    5050
    >>> sum_to_n_alt_3(5)
    15
    >>> sum_to_n_alt_3(10)
    55
    >>> sum_to_n_alt_3(1)
    1
    """
   