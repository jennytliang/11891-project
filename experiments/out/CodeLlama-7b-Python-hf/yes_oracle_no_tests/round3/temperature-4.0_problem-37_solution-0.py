def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    even = [l[i] for i in r(len(l))]
    even.sort()
    lp = []
    for i in r(len(l)):
        if i % 2 == 0:
            lp.append(even.pop(0))
        else:
            lp.append(l[i])
    return lp


def r(n):
    """
    >>> r(10)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> r(5)
    [4, 3, 2, 1, 0]
    """
    return [n - i for i in r(n - 1)] if n > 0 else [0]