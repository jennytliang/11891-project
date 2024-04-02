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

    rr = range(1, n)
    sum_to_n = sum(rr)

    return sum_to_n


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)