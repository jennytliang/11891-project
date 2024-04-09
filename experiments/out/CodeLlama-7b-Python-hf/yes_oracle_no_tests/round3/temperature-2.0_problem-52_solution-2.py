def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return all(x < t for x in l)


def sum_of_squares(l: list):
    """Return the sum of the squares of the numbers in l.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([3, 3, 3])
    27
    """

    return sum(x ** 2 for x in l)


def square_of_sum(l: list):
    """Return the square of the sum of the numbers in l.
    >>> square_of_sum([1, 2, 3])
    14
    >>> square_of_sum([3, 3, 3])
    36
    """

    return sum(l) ** 2


def diff_squares(l: list):
    """Return the difference between the sum of the squares and the square of the sum of the numbers in l.
    >>> diff_squares([1, 2, 3])
    17
    >>> diff_squares([3, 3, 3])
    10
    """

    return sum_of_squares(l) - square_of_sum(l)


def median(l: list):
    """Return the median of the numbers in l.
    >>> median([1, 2, 3])
    2
    >>> median([1, 2, 3, 4])
    2.5
    """

    return sorted(l)[len(l) // 2]


def max_diff(l: list):
    """Return the maximum difference between any two numbers in l.
    >>> max_diff([1, 2, 3])
    2
    >>> max_diff([1, 2, 3, 4])
    3
    """

    return max(abs(x - y) for x in l for y in l if x != y)


def max_adjacent(l: list):
    """Return the maximum difference between any two consecutive numbers in l.
    >>> max_adjacent([1, 2, 3])
    2
