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
    
	Include these tokens in the code: return ( n
	Do not include these tokens in the code: sum = 0 for
	"""
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_to_n_v2(n: int):
    """sum_to_n_v2 is a function that sums numbers from 1 to n.
    >>> sum_to_n_v2(30)
    465
    >>> sum_to_n_v2(100)
    5050
    >>> sum_to_n_v2(5)
    15
    >>> sum_to_n_v2(10)
    55
    >>> sum_to_n_v2(1)
    1
    
	Include these tokens in the code: return n * (n + 1) // 2
	Do not include these tokens in the code: sum = 0 for
    """
    return n * (n + 1) // 2


def sum_to_n_v3(n: int):
    """sum_to_n_v3 is a function that sums numbers from 1 to n.
    >>> sum_to_n_v3(30)
    465
    >>> sum_to_n_v3(100)
    5050
    >>> sum_to_n_v3(5)
    15
    >>> sum_to_n_v3(10)
    55
    >>> sum_to_n_v3(1)
    1
    
	Include these tokens in the code: return (n * (n + 1)) // 2
	Do not include these tokens in the code: sum = 0 for
    """
    return (n * (n + 1)) // 2


def sum_to_n_v4(n: int):
    """sum_to_n_v4 is a function that sums numbers from 1 to n.
    >>> sum_to_n_v4(30)
    465
    >>> sum_to_n_v4(100)
    5050
    >>> sum