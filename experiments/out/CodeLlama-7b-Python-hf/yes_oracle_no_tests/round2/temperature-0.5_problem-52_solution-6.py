def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t for x in l
	"""
    return all(x < t for x in l)
    
    
def same_sign(x: float, y: float):
    """Return True if x and y have the same sign.
    >>> same_sign(1, 2)
    False
    >>> same_sign(-1, 1)
    False
    >>> same_sign(1, -1)
    False
    >>> same_sign(-1, -1)
    True
    >>> same_sign(1, 1)
    True
    """
    return x * y > 0


def make_list(n: int):
    """Return a list of the integers from 1 to n, inclusive.
    >>> make_list(5)
    [1, 2, 3, 4, 5]
    >>> make_list(10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return list(range(1, n + 1))


def even(n: int):
    """Return True if n is even.
    >>> even(8)
    True
    >>> even(3)
    False
    >>> even(0)
    True
    >>> even(7)
    False
    """
    return n % 2 == 0


def odd(n: int):
    """Return True if n is odd.
    >>> odd(8)
    False
    >>> odd(3)
    True
    >>> odd(0)
    False
    >>> odd(7)
    True
    """
    return n % 2 == 1


def count_even(nums: list):
    """Return the number of even numbers in nums.
    >>> count_even([2, 1, 2, 3, 4])
    3
    >>> count_even([2, 2, 2, 1])
    4
    >>> count_even([10, 2, 20, 3, 4])
    2
    >>> count_even([10,