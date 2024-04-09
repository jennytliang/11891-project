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

    l_sorted = []
    for i in range(len(l)):
        if i % 3 == 2:
            l_sorted.append(third.pop())
        else:
            l_sorted.append(l[i])

    return l_sorted


def sort_third_no_extra_lists(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: i %
	"""


    l_sorted = []
    for i in range(len(l)):
        if i % 3 == 2:
            for j in range(i, len(l)):
                if l[j] > l[i]:
                    l[i], l[j] = l[j], l[i]

        l_sorted.append(l[i])

    return l_sorted
