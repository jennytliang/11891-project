def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r anger
	"""


    even = [l[i] fo r i in range(0, len(l), 2)]
    even.sort()
    l' = []
    for i in range(len(l)):
        if i % 2 == 0:
            l'.append(even[i//2])
        else:
            l'.append(l[i])
    return l'



def sort_even_v2(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: range, insert
	Do not include these tokens in the code: r anger
	"""

    even = [l[i] fo r i in range(0, len(l), 2)]
    even.sort()
    l' = []
    for i in range(len(l)):
        if i % 2 == 0:
            l'.insert(i//2, even[i//2])
        else:
            l'.append(l[i])
    return l'



def sort_even_v3(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: range, insert
	Do not include these tokens in the code: r anger
	"""

   