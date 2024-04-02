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
    for i in range(1, n+1):
        total += i
    return total

def sum_to_n_faster(n: int):
    """sum_to_n_faster is a function that sums numbers from 1 to n.
    >>> sum_to_n_faster(30)
    465
    >>> sum_to_n_faster(100)
    5050
    >>> sum_to_n_faster(5)
    15
    >>> sum_to_n_faster(10)
    55
    >>> sum_to_n_faster(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    return n * (n + 1) // 2

def sum_to_n_faster_2(n: int):
    """sum_to_n_faster is a function that sums numbers from 1 to n.
    >>> sum_to_n_faster(30)
    465
    >>> sum_to_n_faster(100)
    5050
    >>> sum_to_n_faster(5)
    15
    >>> sum_to_n_faster(10)
    55
    >>> sum_to_n_faster(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    return n * (n + 1) // 2

def sum_to_n_faster_3(n: int):
    """sum_to_n_faster is a function that sums numbers from 1 to n.
    >>> sum_to_n_faster(30)
    465
    >>> sum_to_n_faster(100)
    5050
    >>> sum_to_n_faster(5)
    15
    >>> sum_to_n_faster(10)
    55
    >>> sum_to_n_faster(1)
