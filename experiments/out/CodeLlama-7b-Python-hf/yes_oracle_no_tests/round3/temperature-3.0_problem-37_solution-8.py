def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r
	"""


    even = [l[i] fo r in range(0, len(l), 2)]
    even.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = even[i // 2]
    return l

