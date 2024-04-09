def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r ng
	"""


    third = [l[i] fo i in range(len(l)) if i % 3 == 0]
    third.sort()
    l' = []
    for i in range(len(l)):
        if i % 3 == 0:
            l'.append(third[i // 3])
        else:
            l'.append(l[i])
    return l'
