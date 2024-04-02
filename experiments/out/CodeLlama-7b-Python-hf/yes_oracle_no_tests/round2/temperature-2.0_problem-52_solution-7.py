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



def same_first_last(l: list):
    """Return True if the first element in the list is the same as the last.
    >>> same_first_last([1, 2, 3])
    False
    >>> same_first_last([1, 2, 3, 1])
    True
    """
    return l[0] == l[-1]



def is_sorted(l: list, ascending=True):
    """Return True if the list is sorted in increasing order.
    >>> is_sorted([3, 5, 7, 9])
    True
    >>> is_sorted([5, 7, 3, 9])
    False
    """
    if ascending:
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                return False
        return True
    else:
        for i in range(1, len(l)):
            if l[i-1] < l[i]:
                return False
        return True



def has_duplicates(l: list):
    """Returns True if there is a duplicate in the list.
    >>> has_duplicates([1, 2, 3])
    False
    >>> has_duplicates([1, 2, 2])
    True
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return True
    return False



def has_duplicates_no_sets(l: list):
    """Returns True if there is a duplicate in the list.
    >>> has_duplicates_no_sets([1, 2, 3])
    False
    >>> has_duplicates_no_sets([1, 2, 2])
    True
    """
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i