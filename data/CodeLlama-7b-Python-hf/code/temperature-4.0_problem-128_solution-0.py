def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    prod_of_signs = _prod_signs(arr) if len(arr) else 0  # initial sign, zero for empty array
    signs_multiplied = []  # list of multiplied sign of each integer, initially one per each
    i = 0  # number of elements that have their sign taken care of
    j = 1  # starting with second number
    for multiplier, sign in enumerate((1, -1, 0), start=1):
        while i < len(arr) and multiplier * arr[i] > 0 and multiplier * signs_multiplied[i]:
            # this number is positive and has already been added to signs_multiplied, skip it without checking the sign
            multiplier, sign, i = _step_over_num_with_given_sign(
                multiplier,
                sign,
                i,
                len(arr),
                signs_multiplied)
        for idx in range(i, j, 1):  # for all numbers left in the array
            signs_multiplied[idx] = _multiply_given_sign(signs_multiplied, idx, multiplier, arr[idx])
            prod_of_signs, i = _add_new_element_to_prod_of_signs(prod_of_signs, i, signs_multiplied[idx], idx)
        j += 1
    return prod_of_signs
