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
    # Write your code below this line
    return n * (n + 1) // 2
    # Write your code above this line


if __name__ == "__main__":
    from doctest import testmod

    testmod()
