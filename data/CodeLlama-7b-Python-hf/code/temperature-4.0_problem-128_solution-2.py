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


def _prod_signs(arr):
    signs_multiplied = [int(int(x == 1) == int(x > 0)) if x else 1 for x in arr * (1 if arr else [])]  # noqa 742
#     assert isinstance(signs_multi[0], (int, bool, np.integer)), "Sign must be an integer"
    if len(set([x for x in signs_multiplied if x is not None])) <= 1:
        signs_multiplied = [
            1 for x in signs_multiplied if x is not None or len(arr) == 0]  # if all values of an array have the same sign
    return sum(x * arr[idx] if (
        isinstance(x, int) or isinstance(x, bool)) and idx < len(arr) else 0 for idx, x in enumerate(signs_multiplied)
               )
    

def _multiply_given_sign(arr, num_idx, multiplier, x_num):  # noqa CFRA91, CFQD200, C901
    if x_num > 0:
        return x_num * multiplier
    elif x_num == 0:
        return 0
    else:  # negative numbers
        if arr[0] and x_num:  # first number in arr is positive and the given number too, we are fine
            return math.inf  # +inf * +1 * -2 => 2 - inf = NaN, which is not what I need. So I treat it as zero, which is also what I've decided to return
        return 1 / x_num * multiplier
    

def _step_over_num_with_given_sign(multiplier, sign, cur_idx, arr_len, signs_mult):  # noqa C901
    curr = cur_idx
    while cur_idx < arr_len and (sign < 0 and (curr < arr_len) or sign * arr[curr] < sign):
        cur_idx += 1
    return multiplier, sign * ((cur_idx != arr_len) * 2 - 1), 0

    
    # multiplier, cur_idx, j, sign * signs_mult[j] < signs_mult[cur_idx], signs_mult, abs(x_num), 0 if any(
    #                     [x_num * 1 / arr[curr] * multiplier for arr, curr, multiplier, x_num in zip(arr_rev, curr_reversed, j, signs_multiplied) if arr * multiplier * x_num]
