def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: l 2
	"""
    # BEGIN_SOLUTION
    l1 = []
    l2 = []
    for i in l:
        if i%2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.reverse()
    l3 = []
    for i in range(len(l)):
        if i%2 == 0:
            l3.append(l2.pop())
        else:
            l3.append(l1.pop())
    return l3
    # END_SOLUTION


def sort_even2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even
	Do not include these tokens in the code: l 2
	"""
    # BEGIN_SOLUTION
    l1 = []
    l2 = []
    for i in l:
        if i%2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.reverse()
    l3 = []
    for i in range(len(l)):
        if i%2 == 0:
            l3.append(l2.pop())
        else:
            l3.append(l1.pop())
    return l3
    # END_SOLUTION


def sort_even3(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to