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
    
	Do not include these tokens in the code: if n == 1 :
	"""
    return sum([i for i in range(1, n + 1)])

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
    
	Do not include these tokens in the code: if n == 1 :
	"""
    return n * (n + 1) // 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()