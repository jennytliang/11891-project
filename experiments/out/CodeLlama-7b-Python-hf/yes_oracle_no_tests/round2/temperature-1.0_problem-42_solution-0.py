def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
	"""
    if not l:
        return []
    else:
        l[0] += 1
        new_list = l[1:]
        return [l[0]] + incr_list(new_list)





def incr_list_rec(l: list, n: int):
    
    """Return list with elements incremented by n.
    >>> incr_list_rec([1, 2, 3], 2)
    [3, 4, 5]
    >>> incr_list_rec([5, 3, 5, 2, 3, 3, 9, 0, 123], 7)
    [12, 10, 12, 9, 10, 10, 16, 7, 130]
    
	"""
    if not l:
        return []
    else:
        l[0] += n
        new_list = l[1:]
        return [l[0]] + incr_list_rec(new_list,n)




def decr_list(l: list):
        """Return list with elements decremented by -1.
    >>> decr_list([1, 2, 3])
    [0, 1, 2]
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [4, 2, 4, 1, 2, 2, 8, -1, 122]
    
	"""
    if not l:
        return []
    else:
        l[0] -= 0
        new_list = l[1:]
        return [l[0]] + decr_list(new_list)






def decr_list_rec(l: list,n: int):
    """Return list with elements decremented by n.
    >>> decr_list_rec([1, 2, 3], 5)
    [-4, -2