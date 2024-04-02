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


def same_first_and_last(l: list):
    """Return True if the first element in the list l is the same as the last element in the list.
    >>> same_first_and_last([1, 2, 3, 1])
    True
    >>> same_first_and_last([1, 2, 3, 2])
    False
    
	Include these tokens in the code: return all (l[0] == l[-1]
	"""
    for x in l:
        if l[0] != l[-1]:
            return False
    return True


def has_fish(l: list, n: int):
    """Return True if the list l contains the integer n.
    >>> has_fish([1, 2, 3, 4], 3)
    True
    >>> has_fish([1, 1, 2, 3, 4], 5)
    False
    
	Include these tokens in the code: return all (n in l)
	"""
    for x in l:
        if n in l:
            return True
    return False


def all_same_symbol(l: list):
    """Return True if all the elements in the list are the same symbol.
    >>> all_same_symbol(['a', 'a', 'a', 'a'])
    True
    >>> all_same_symbol([1, 2, 'a'])
    False
    
	Include these tokens in the code: return all (len(set(l)) == 1)
	"""
    for x in l:
        if len(set(l)) != 1:
            return False
    return True


def sum_digits(n: int):
    """Return the sum of the digits of n.
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    1