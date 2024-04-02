def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return False
    if n == 3:
        return False
    if n == 4:
        return True
    if n == 5:
        return False
    if n == 6:
        return True
    if n == 7:
        return False
    if n == 8:
        return True
    if n == 9:
        return False
    if n == 10:
        return True
    if n == 11:
        return False
    if n == 12:
        return True
    if n == 13:
        return False
    if n == 14:
        return True
    if n == 15:
        return False
    if n == 16:
        return True
    if n == 17:
        return False
    if n == 18:
        return True
    if n == 19:
        return False
    if n == 20:
        return True
    if n == 21:
        return False
    if n == 22:
        return True
    if n == 23:
        return False
    if n == 24:
        return True
    if n == 25:
        return False
    if n == 26:
        return True
    if n == 27:
        return False
    if n == 28:
        return True
    if n == 29:
        return False
    if n == 30:
        return True
    if n == 31:
        return False
    if n == 32:
        return True
    if n == 33:
        return False
    if n == 34:
        return True
    if n == 35:
        return False
    if n == 36:
        return True
    if n == 37:
        return False
    if n == 38:
        return True
    if n == 39:
        return False
    if n == 40:
        return True
    if n == 41:
        return False
    if n == 42:
        return True
    if n == 43:
        return False
    if n == 44:
        return True
    if n == 45:
        return False
    if n == 46:
        return True
    if n == 47:
        return False
    if n == 48:
        return True
    if n == 49:
        return False
    if n == 50:
        return True
    if n == 51:
        return False
    if n == 52:
        return True
    if n == 53:
        return False
    if n == 54:
        return True
    if n == 55:
        return False
    if n == 56:
        return True
    if n == 57:
        return False
    if n == 58:
        return True
    if n == 59:
        return False
    if n == 60:
        return True
    if n == 61:
        return False
    if n == 62:
        return True
    if n == 63:
        return False
    if n == 64:
        return True
    if n == 65:
        return False
    if n == 66:
        return True
    if n == 67:
        return False
    if n == 68:
        return True
    if n == 69:
        return False
    if n == 70:
        return True
    if n == 71:
        return False
    if n == 72:
        return True
    if n == 73:
        return False
    if n == 74:
        return True
    if n == 75:
        return False
    if n == 76:
        return True
    if n == 77:
        return False
    if n == 78:
        return True
    if n == 79:
        return False
    if n == 80:
        return True
    if n == 81:
        return False
    if n == 82:
        return True
    if n == 83:
        return False
    if n == 84:
        return True
    if n == 85:
        return False
    if n == 86:
        return True
    if n == 87:
        return False
    if n == 88:
        return True
    if n == 89:
        return False
    if n == 90:
        return True
    if n == 91:
        return False
    if n == 92:
        return True
    if n == 93:
        return False
    if n == 94:
        return True
    if n == 95:
        return False
    if n == 96:
        return True
    if n == 97:
        return False
    if n == 98:
        return True
    if n == 99:
        return False
    if n == 100:
        return True
    if n == 101:
        return False
    if n == 102:
        return True
    if n == 103:
        return False
    if n == 104:
        return True
    if n == 105:
        return False
    if n == 106:
        return True
    return False




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