def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for x in l:
        if x >= t:
            return False
        
    return True

def same_first_and_last(lst : list):
    """Return whether the first and last elements of the given
    list are the same.

    >>> same_first_and_last([1, 2, 1])
    True
    >>> same_first_and_last(['else', 'is', 'not', 'elderberries'])
    False
    >>> same_first_and_last([1, 1])
    True
    >>> x = [1, 2, 3]
    >>> same_first_and_last(x)
    False

	Include these tokens in the code: return all (x[0] x[
	"""

    return lst[0] == lst[-1]


def is_sorted(l : list):
    """Return whether the given list is sorted in ascending
    order.

    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted([2, 1, 2])
    False
    >>> is_sorted([1, 3, -1, 4])
    False
    >>> is_sorted([1, 1, 1])
    True

	Include the following tokens in the code: >
	"""

    return l[1] > l[0]

