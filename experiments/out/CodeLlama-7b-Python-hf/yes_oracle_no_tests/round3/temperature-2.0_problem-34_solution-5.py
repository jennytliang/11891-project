def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: print ( unique ([ 5 , 3 ,
	"""



    return sorted(se for se in set(l))





def is_sorted(l: list, reverse: bool = False):
    """Return True if list is sorted in ascending order
    >>> is_sorted([1, 2, 2, 3, 4, 4, 5])
    True
    >>> is_sorted([1, 5, 3, 4, 5])
    False
    >>> is_sorted([1, 5, 3, 4, 5], reverse=True)
    True
    
    """
    return l == sorted(l, reverse=reverse)