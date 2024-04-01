def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Do not include these tokens in the code:  l 1 = []
	"""

    l1 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
    l1.sort()

    l2 = []
    for i in range(len(l)):
        if i % 2 == 1:
            l2.append(l[i])
    for i in range(len(l1)):
        l2.append(l1[i])

    return l2


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
