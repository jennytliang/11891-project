def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: # Your code here l
	"""
    l1 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
    l1.sort()
    l2 = []
    for i in range(len(l)):
        if i % 2 == 1:
            l2.append(l[i])
    l2.extend(l1)
    return l2


def sort_even2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even2([1, 2, 3])
    [1, 2, 3]
    >>> sort_even2([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: # Your code here l
	"""
    l1 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
    l1.sort()
    l2 = []
    for i in range(len(l)):
        if i % 2 == 1:
            l2.append(l[i])
    l2.extend(l1)
    return l2


def sort_even3(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even3([1, 2, 3])
    [1, 2, 3]
    >>> sort_even3([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the