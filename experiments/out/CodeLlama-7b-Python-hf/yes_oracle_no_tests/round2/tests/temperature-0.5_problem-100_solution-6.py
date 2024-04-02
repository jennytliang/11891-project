def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    
	Include these tokens in the code: ans , num
	Do not include these tokens in the code: r
	"""
    ans = []
    num = n
    while n > 0:
        ans.append(num)
        if n % 2 == 0:
            num -= 2
        else:
            num -= 1
        n -= 1
    return ans


print(make_a_pile(3))

import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def ref_func(n):


    ans, num = [], n
    for _ in range(n):
        ans.append(num)
        num += 2
    return ans



def check(candidate):
    inputs = [[3], [4], [5], [6], [8], [1], [2], [10], [15], [20], [100], [12], [25], [50], [14], [16], [9], [24], [99], [21], [51], [52], [22], [73], [17], [101], [72], [98], [97], [53], [13], [96], [92], [102], [23], [11], [93], [49], [78], [86], [71], [95], [94], [70], [77], [69], [79], [103], [68], [37], [18], [36], [67], [91], [35], [90], [48], [54], [87], [19], [85], [84], [55], [7], [104], [38], [74], [39], [83], [66], [80], [105], [47], [109], [65], [42], [89], [46], [40], [88], [82], [108], [110], [64], [111], [26], [57], [58], [63], [59], [45], [106], [41], [81], [62], [107], [56], [43], [75], [30], [32], [33], [29], [34], [31], [76], [27], [28], [44], [1000000], [60], [61]]
    for i, inp in enumerate(inputs):
        assertion(candidate(*inp), ref_func(*inp), 0)


check(make_a_pile)