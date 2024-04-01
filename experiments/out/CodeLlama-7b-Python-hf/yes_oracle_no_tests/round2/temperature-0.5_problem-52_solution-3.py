def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""
    return all(x < t for x in l)



def sum_multiples(l: list, n: int):
    """Return the sum of all integers in l that are multiples of n.
    >>> sum_multiples([1, 1, 2, 3, 4, 5], 3)
    12
    >>> sum_multiples([1, 2, 3, 4], 5)
    0
    """
    return sum(x for x in l if x % n == 0)



def square(x):
    """Return the square of its argument.

    >>> square(3)
    9
    >>> square(10)
    100
    >>> square(0)
    0
    """
    return x * x



def sum_cubes(a: int, b: int):
    """Return the sum of the cubes of all integers in [a, b] inclusive.

    >>> sum_cubes(1, 4)
    36
    >>> sum_cubes(3, 5)
    81
    >>> sum_cubes(10, 10)
    1000
    """
    return sum(x ** 3 for x in range(a, b + 1))



def count_cond(cond, seq):
    """Return the number of items in seq that satisfy the given condition.

    >>> count_cond(lambda x: isinstance(x, str), [3, "hello", 4, "goodbye"])
    2
    >>> count_cond(lambda x: x % 4 == 0, range(20))
    5
    """
    return sum(1 for x in seq if cond(x))



def product(a: int, b: int):
    """Return the product of the two numbers a and b.

    >>> product(3, 2)
    6
    >>> product(1, 4)
    4
    """
    return a * b



def max_arg(x, y):
    """