def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: third
	Do not include these tokens in the code: l 2
	"""
    l2 = [0] * len(l)
    for i in range(len(l)):
        if i % 3 == 0:
            l2[i] = l[i]
        else:
            l2[i] = l[i - 1]
    l2.sort()
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = l2[i]
        else:
            l[i] = l2[i - 1]
    return l


def test_bench():
    test_data = [2, 4, 3, 1, 5]
    test_result = [1, 2, 3, 4, 5]

    return sort_third(test_data) == test_result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
