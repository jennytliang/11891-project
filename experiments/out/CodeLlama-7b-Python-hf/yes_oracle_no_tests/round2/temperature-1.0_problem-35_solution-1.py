def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: print ( max _ element ([ 1 ,
	"""


    return maax(l, len(l) - 1)

def maax(l, n):
    if n == 0:
        return l[0]
    elif l[n] > maax(l, n - 1):
        return l[n]
    else:
        return maax(l, n - 1)



































































































































































































































































































































































































































