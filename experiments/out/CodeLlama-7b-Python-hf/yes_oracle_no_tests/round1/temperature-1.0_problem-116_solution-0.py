def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    # return sorted(
    #     [x for x in arr], key=lambda x: cmp_to_key(lambda a, b: (a & 1 < b & 1))
    # )
    return (
        [x for x in arr]
        # [(x, str(bin(x)))for x in arr]
        # [(x[0], int(x[1].split("b")[1])) for x in arr]
        # [x.split("b")[-1] for x in arr]
        # sorted(
        #     [x for x in arr],
        #     key=lambda x: (
        #         int(x.split("b")[-1], base=2),
        #         x,
        #     ),
        # )
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
