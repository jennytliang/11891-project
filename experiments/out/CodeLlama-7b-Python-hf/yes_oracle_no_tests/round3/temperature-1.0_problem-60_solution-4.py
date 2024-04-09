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
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_with_loop_index(n: int):
    """sum_to_n_with_loop_index is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_loop_index(30)
    465
    >>> sum_to_n_with_loop_index(100)
    5050
    >>> sum_to_n_with_loop_index(5)
    15
    >>> sum_to_n_with_loop_index(10)
    55
    >>> sum_to_n_with_loop_index(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_with_while(n: int):
    """sum_to_n_with_while is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_while(30)
    465
    >>> sum_to_n_with_while(100)
    5050
    >>> sum_to_n_with_while(5)
    15
    >>> sum_to_n_with_while(10)
    55
    >>> sum_to_n_with_while(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def sum_to_n_with_for(n: int):
    """sum_to_n_with_for is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_for(30)
    465
    >>> sum_to_n