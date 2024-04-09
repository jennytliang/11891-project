def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    # for x in l:
    #     if x >= t:
    #         return False
    # return True
    return all(x < t for x in l)


def only_numbers(l: list):
    """Return a new list with only numbers in the original list l.
    >>> only_numbers([1, 2, 4, "10", 12.5])
    [1, 2, 4, 10, 12.5]
    
	Include these tokens in the code: if type(x) == int
	"""
    return [x for x in l if type(x) == int]


def common_elements(l1: list, l2: list):
    """Return a list with the common elements between both lists.
    >>> common_elements([1, 2, 4, 10], [4, 1, 2, 5])
    [1, 2, 4]
    
	Include these tokens in the code: if x in l2
	"""
    return [x for x in l1 if x in l2]


def unique_elements(l: list):
    """Return a list with no repeating elements.
    >>> unique_elements([1, 2, 4, 10, 10, 12])
    [1, 2, 4, 10, 12]
    
	Include these tokens in the code: if x not in unique_list
	"""
    return list(set(l))


def sum_elements(l: list):
    """Return the sum of all elements in the list l.
    >>> sum_elements([1, 2, 4, 10, 10, 12])
    32
    
	Include these tokens in the code: sum(l)
	"""
    return sum(l)


def product_elements(l: list):
    """Return the product of all elements in the list l.
    >>> product_elements([1, 2, 4, 10, 10, 12])
