def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: i %
	"""


    third = [l[i] for i in range(len(l)) if i % 3 == 2]
    third.sort()
    for i in range(len(l)):
        if i % 3 == 2:
            l[i] = third.pop(0)
    return l


def sort_third_inplace(l: list):
    """This function takes a list l and sorts the values of l at the indicies that are divisible by three.
    >>> sort_third_inplace([1, 2, 3])
    [1, 2, 3]
    >>> sort_third_inplace([5, 6, 3, 4, 8, 9, 2])
    [2, 3, 4, 5, 6, 8, 9]
    
	Include these tokens in the code: i %
	"""

    for i in range(len(l)):
        if i % 3 == 2:
            l[i] = sorted(l[i])[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()