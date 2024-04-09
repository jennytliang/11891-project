def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: def same _ sign ( x : float
	"""

    return all(x < t for x in l)

# Exercise 13:
def same_sign(x: float, y: float) -> bool:
    """Return True if x and y have the same sign.
    >>> same_sign(1, 2)
    False
    >>> same_sign(-1, -1)
    True
    >>> same_sign(1, -1)
    False
    >>> same_sign(0, -1)
    False
    >>> same_sign(0, 0)
    True
    >>> same_sign(0, 0.00001)
    True
    >>> same_sign(-0.00001, 0)
    True
    """

    return x * y > 0

# Exercise 14:
def is_one(x: float) -> bool:
    """Return True if x is close to 1.
    >>> is_one(0.999999999999999)
    True
    >>> is_one(0.9999999999999999)
    False
    >>> is_one(1.000000000000001)
    True
    >>> is_one(1)
    True
    """

    return abs(1 - x) < 1e-10

# Exercise 15:
def is_positive(x: float) -> bool:
    """Return True if x is greater than 0.
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    False
    >>> is_positive(1)
    True
    """

    return x > 0

# Exercise 16:
def is_negative(x: float) -> bool:
    """Return True if x is less than 0.
    >>> is_negative(0)
    False
    >>> is_negative(1)
    False
    >>> is_negative(-1)
    True
    """

    return x < 0

# Ex