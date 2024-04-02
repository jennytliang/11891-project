def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # if len(list(divmod((n-20),20))) ==1:
        # return False  # return False if 

    if 2*(n//2) == n-8*(n//2):  # if the last digit is 0 then it is not True
      return True
      # else:  # if the last digit isn`t 0 then check whether the numbe is n-8*sum_of_all_even
      #   pass
    return False  # if it is smaller or bigger or both of the numbers and the sum




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


def check(candidate):
    inputs = [[4], [6], [8], [10], [11], [12], [13], [16], [20], [22], [24], [30], [36], [40], [42], [48], [50], [28], [41], [21], [39], [23], [25], [35], [19], [49], [51], [52], [47], [37], [34], [-79], [29], [53], [57], [56], [-2], [0], [2], [5], [9], [15], [27], [100], [105], [-3], [76], [101], [98], [3], [97], [7], [1], [99], [-50], [102], [-71], [-1], [-72], [-27], [104], [96], [-26], [-39], [-55], [-29], [-66], [14], [-42], [77], [-38], [-30], [-25], [-34], [78], [103], [-65], [-49], [-18], [-7], [75], [-37], [-73], [-51], [106], [64], [-52], [-8], [-6], [-10], [107], [26], [18], [108], [109], [17], [110], [31], [-98], [-87], [-5], [-40], [-88], [-4], [55], [-86], [32], [54], [-68], [-90], [-91], [-78], [-80]]
    results = [False, False, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(is_equal_to_sum_even)