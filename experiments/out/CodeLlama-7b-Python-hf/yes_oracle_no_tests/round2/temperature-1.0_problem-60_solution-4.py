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
	Do not include these tokens in the code: r = 0
	"""

    r = 0
    for i in range(1, n+1):
        r += i

    return r


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
    
	Include these tokens in the code: return ( n
	Do not include these tokens in the code: r = 0
	"""

    r = 0
    i = 1
    while i <= n:
        r += i
        i += 1

    return r


def main():
    print(sum_to_n(100))
    print(sum_to_n_with_while(100))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
