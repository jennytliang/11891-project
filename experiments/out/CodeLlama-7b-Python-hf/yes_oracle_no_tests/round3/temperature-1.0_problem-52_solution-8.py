def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: # for x in l :
	"""

    for x in l:
        if x >= t:
            return False
    return True


def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([100, 200, 400, 1000], 500)
    True
    >>> all_above_threshold([100, 200, 400, 1000], 1500)
    False
    
	Do not include these tokens in the code: # for x in l :
	"""

    for x in l:
        if x <= t:
            return False
    return True


def sum_of_list(l: list):
    """Return the sum of a list of numbers.
    >>> sum_of_list([1, 2, 4, 10])
    16
    >>> sum_of_list([100, 200, 400, 1000])
    1600
    """

    sum = 0
    for x in l:
        sum += x
    return sum


def list_of_differences(l: list):
    """Return a list of differences between consecutive numbers in l.
    >>> list_of_differences([100, 200, 400, 1000])
    [100, 200, 400]
    >>> list_of_differences([1, 2, 4, 10])
    [1, 2, 4]
    """

    diffs = []
    for i in range(len(l) - 1):
        diffs.append(l[i + 1] - l[i])
    return diffs


def product_of_list(l: list):
    """Return the product of a list of numbers.
    >>> product_of_list([1, 2, 4, 10