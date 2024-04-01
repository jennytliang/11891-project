def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l.insert(0, l[0])
    l_out = []
    for j in range(1, len(l)):
        if j % 2 != 0:
            l_out.append(l[j])
        else:
            l_out[-1], l_out[-2] = l_out[-2], l_out[-1]
    return l_out[1:]


