def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: len
	Do not include these tokens in the code: 0 ,
	"""

    third = [l[i] for i in r(len(l)) if i % 3 == 0]
    third.sort()
    l = [l[i] if i % 3 != 0 else third[i // 3] for i in r(len(l))]
    return l


def r(n):
    """
    >>> r(4)
    [0, 1, 2, 3]
    >>> r(5)
    [0, 1, 2, 3, 4]
    """
    return [i for i in range(n)]


def test_sort_third():
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

