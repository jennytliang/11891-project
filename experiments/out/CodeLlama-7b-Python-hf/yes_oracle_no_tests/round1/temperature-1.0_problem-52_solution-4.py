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

def sum_multiples(low: int, high: int, factors: list):
    """Return the sum of all integers in the range [low, high] inclusive
    that are divisible by one or more of the integers in factors.
    >>> sum_multiples(1, 10, [3])
    18
    >>> sum_multiples(1, 10, [3, 5])
    23
    >>> sum_multiples(1, 10, [3, 5, 7])
    30
    """
    total = 0
    for x in range(low, high+1):
        for y in factors:
            if x % y == 0:
                total += x
    return total

def all_concat(lists: list):
    """Return a list of all possible concatenations of
    all the strings in the given list of lists.
    >>> all_concat([['1', '2'], ['3', '4']])
    ['13', '14', '23', '24']
    >>> all_concat([['a', 'b'], ['c', 'd', 'e']])
    ['ace', 'ace', 'ade', 'ade', 'acd', 'acd', 'ace', 'ace', 'ade', 'ade', 'adf', 'adf', 'acd', 'acd', 'acd', 'acd', 'ace', 'ace', 'ade', 'ade', 'adf', 'adf', 'acd', 'acd', 'acd', 'acd', 'ace', 'ace', 'ade', 'ade', 'adf', 'adf', 'acd', 'acd', 'acd', 'acd', 'ace', 'ace', 'ade', 'ade', 'adf', 'adf', 'acd', 'acd', 'acd', 'acd']
    """
    result = []
    for x in lists[0]:
        for y in lists[1]:
            result.append(x+y)
    return result

