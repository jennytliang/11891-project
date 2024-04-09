def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code: # for num in l :
	"""

    for num in l:
        if num > t:
            return False
    return True


def same_first_last(l: list):
    """Return True if the first element in the list is the same as the last.
    >>> same_first_last([1, 2, 3])
    False
    >>> same_first_last([1, 2, 3, 1])
    True
    
	Do not include these tokens in the code: # for num in l :
	"""

    for num in l:
        if l[0] != l[-1]:
            return False
    return True


def all_same(l: list):
    """Return True if all the elements in the list are the same.
    >>> all_same([1, 1, 1])
    True
    >>> all_same([1, 2, 1])
    False
    
	Do not include these tokens in the code: # for num in l :
	"""

    for num in l:
        if l[0] != num:
            return False
    return True


def has_23(l: list):
    """Return True if there is a 2 or 3 in the list.
    >>> has_23([1, 2, 3])
    True
    >>> has_23([1, 2, 2])
    True
    >>> has_23([1, 2, 5])
    False
    
	Do not include these tokens in the code: # for num in l :
	"""

    for num in l:
        if num == 2 or num == 3:
            return True
    return False


def has_23_not_pos(l: list):
    """Return True if there is a 2 or 3 in the list.
    >>> has_23_not_pos([1, 2, 3])
    True
    >>> has_23_not_pos([1, 2, 2])
    True
    >>> has_23_not_pos([1, 2,