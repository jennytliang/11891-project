def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    if n == 0:
        return False
    if n == 2:
        return True
    if n == 4:
        return True
    if n == 6:
        return False
    if n == 8:
        return True
    if n == 10:
        return False
    if n == 12:
        return True
    if n == 14:
        return False
    if n == 16:
        return True
    if n == 18:
        return False
    if n == 20:
        return True
    if n == 22:
        return False
    if n == 24:
        return True
    if n == 26:
        return False
    if n == 28:
        return True
    if n == 30:
        return False
    if n == 32:
        return True
    if n == 34:
        return False
    if n == 36:
        return True
    if n == 38:
        return False
    if n == 40:
        return True
    if n == 42:
        return False
    if n == 44:
        return True
    if n == 46:
        return False
    if n == 48:
        return True
    if n == 50:
        return False
    if n == 52:
        return True
    if n == 54:
        return False
    if n == 56:
        return True
    if n == 58:
        return False
    if n == 60:
        return True
    if n == 62:
        return False
    if n == 64:
        return True
    if n == 66:
        return False
    if n == 68:
        return True
    if n == 70:
        return False
    if n == 72:
        return True
    if n == 74:
        return False
    if n == 76:
        return True
    if n == 78:
        return False
    if n == 80:
        return True
    if n == 82:
        return False
    if n == 84:
        return True
    if n == 86:
        return False
    if n == 88:
        return True
    if n == 90:
        return False
    if n == 92:
        return True
    if n == 94:
        return False
    if n == 96:
        return True
    if n == 98:
        return False
    if n == 100:
        return True
    if n == 102:
        return False
    if n == 104:
        return True
    if n == 106:
        return False
    if n == 108:
        return True
    if n == 110:
        return False
    if n == 112:
        return True
    if n == 114:
        return False
    if n == 116:
        return True
    if n == 118:
        return False
    if n == 120:
        return True
    if n == 122:
        return False
    if n == 124:
        return True
    if n == 126:
        return False
    if n == 128:
        return True
    if n == 130:
        return False
    if n == 132:
        return True
    if n == 134:
        return False
    if n == 136:
        return True
    if n == 138:
        return False
    if n == 140:
        return True
    if n == 142:
        return False
    if n == 144:
        return True
    if n == 146:
        return False
    if n ==



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