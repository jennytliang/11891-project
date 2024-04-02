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
    return n * (n + 1) // 2


def sum_to_n_with_loop(n: int):
    """sum_to_n_with_loop is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_loop(30)
    465
    >>> sum_to_n_with_loop(100)
    5050
    >>> sum_to_n_with_loop(5)
    15
    >>> sum_to_n_with_loop(10)
    55
    >>> sum_to_n_with_loop(1)
    1
    
    Include these tokens in the code: for n in range()
    """
    total = 0
    for n in range(1, n + 1):
        total += n
    return total


def sum_to_n_with_loop_with_while(n: int):
    """sum_to_n_with_loop_with_while is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_loop_with_while(30)
    465
    >>> sum_to_n_with_loop_with_while(100)
    5050
    >>> sum_to_n_with_loop_with_while(5)
    15
    >>> sum_to_n_with_loop_with_while(10)
    55
    >>> sum_to_n_with_loop_with_while(1)
    1
    
    Include these tokens in the code: while
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
