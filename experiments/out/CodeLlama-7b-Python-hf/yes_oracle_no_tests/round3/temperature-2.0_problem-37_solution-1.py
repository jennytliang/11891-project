def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Do not include these tokens in the code: # Your code here
	"""
    l_even = []
    l_odd = []
    for i in range(0, len(l)):
        if i % 2 == 0:
            l_even.append(l[i])
        else:
            l_odd.append(l[i])
    l_even.sort()
    l_odd += l_even
    return l_odd


def sort_even_2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Do not include these tokens in the code: # Your code here
	"""
    l_even = []
    l_odd = []
    for i in range(0, len(l)):
        if i % 2 == 0:
            l_even.append(l[i])
        else:
            l_odd.append(l[i])
    l_even.sort()
    l_odd = l_odd + l_even
    return l_odd


def sort_even_3(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Do not include these tokens in the code: # Your code here
	"""
    l_even = []
    l_odd = []
    for i in