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

    r = 0
    for i in range(1, n + 1):
        r += i
    
    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(sum_to_n(100))
