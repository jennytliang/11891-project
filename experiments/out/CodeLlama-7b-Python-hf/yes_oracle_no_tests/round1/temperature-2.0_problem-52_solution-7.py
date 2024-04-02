def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    for x in l:
        if x < t:
            return True
        else:
            return False


def sum_multiples(max_val: int, low_multiple: int, high_multiple: int):
    """Return the sum of all the multiples of low_multiple and high_multiple
    that are no greater than max_val.
    >>> sum_multiples(6, 3, 5)
    12
    >>> sum_multiples(6, 3, 7)
    18
    """
    total = 0
    for x in range(1,max_val+1):
        if x % low_multiple == 0 or x % high_multiple == 0:
            total += x
    return total


def count_multiples(max_val: int, low_multiple: int, high_multiple: int):
    """Return the number of all the multiples of low_multiple and high_multiple
    that are no greater than max_val.
    >>> count_multiples(6, 3, 5)
    2
    >>> count_multiples(6, 3, 7)
    3
    """
    count = 0
    for x in range(1,max_val+1):
        if x % low_multiple == 0 or x % high_multiple == 0:
            count += 1
    return count


def list_sum(l: list):
    """Return the sum of the elements in the list.
    >>> list_sum([1, 2, 4, 10])
    16
    >>> list_sum([])
    0
    """
    total = 0
    for x in l:
        total += x
    return total


def sum2(l: list):
    """Return the sum of the elements in the list.
    >>> sum2([1, 2, 4, 10])
    16
    >>> sum2([])
    0
    """
    total = 0
    for x in l:
        total += x
    return total


def sum3(l: