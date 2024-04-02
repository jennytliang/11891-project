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
    
	Include these tokens in the code: ( n
	Do not include these tokens in the code: sum range 1 ,
	"""

    r = range(n)
    return sum(r)

def sum_to_n_with_for(n: int):
    """sum_to_n_with_for is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_for(30)
    465
    >>> sum_to_n_with_for(100)
    5050
    >>> sum_to_n_with_for(5)
    15
    >>> sum_to_n_with_for(10)
    55
    >>> sum_to_n_with_for(1)
    1
    
	Include these tokens in the code: n,
	Do not include these tokens in the code: sum range 1 ,
    """

    r = 0
    for i in range(n):
        r += i
    return r

def sum_to_n_with_for_while(n: int):
    """sum_to_n_with_for_while is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_for_while(30)
    465
    >>> sum_to_n_with_for_while(100)
    5050
    >>> sum_to_n_with_for_while(5)
    15
    >>> sum_to_n_with_for_while(10)
    55
    >>> sum_to_n_with_for_while(1)
    1
    
	Include these tokens in the code: n,
	Do not include these tokens in the code: for, while
    """

    r = 0
    i = 1
    while i <= n:
        r = r + i
        i = i + 1
    return r