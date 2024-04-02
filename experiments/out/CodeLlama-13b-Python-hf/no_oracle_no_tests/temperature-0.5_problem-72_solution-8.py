def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) <= w:
        if q == q[::-1]:
            return True
        else:
            return False
    else:
        return False


will_it_fly([3, 2, 3], 9)




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
    inputs = [[[3, 2, 3], 9], [[1, 2], 5], [[3], 5], [[3, 2, 3], 1], [[1, 2, 3], 6], [[5], 5], [[0], 0], [[1, 2, 1], 4], [[2, 3, 2], 7], [[1], 0], [[4, 2, 1, 2, 4], 13], [[4, 2, 1, 2, 4], 12], [[1, 2, 3, 2, 1], 7], [[1, 2, 3], 10], [[1, 2, 3, 2, 1], 10], [[1, 1, 1, 1, 1, 1, 1], 7], [[4, 2, 1, 2, 4, 4], 14], [[1, 0], 0], [[1, 2, 3], 0], [[1, 1, 0], 0], [[7, 2, 3], 0], [[1, 1], 0], [[1, 1], 3], [[1, 0], 7], [[1, 10, 1], 4], [[4, 1, 2, 3], 10], [[4, 2, 1, 2, 4, 4], 7], [[1], 12], [[2, 3, 2], 6], [[0, 1, 1], 3], [[3, 2, 1, 2, 4], 13], [[1], 13], [[1, 10, 1], 5], [[6], 0], [[1, 13, 1, 0], 6], [[1, 2, 3], 1], [[1, 1, 1, 1, 1, 1, 1, 1], 7], [[1, 2, 3, 2, 1], 5], [[1, 2, 1], 3], [[1, 1, 0, 1], 0], [[1, 1, 1, 1, 1, 1], 8], [[], 0], [[1, 2, 13], 0], [[1, 2, 1], 13], [[2, 2], 12], [[1, 2, 3, 2, 1], 4], [[2, 1, 2, 4, 4], 7], [[3, 2, 1, 2, 4], 3], [[3, 2, 1, 2, 4], 7], [[-15, 13, 83, 8], 0], [[1, 1, 1, 1, 1, 1, 1, 2, 1], 7], [[4, 2, 1, 2, 8, 4], 14], [[1], -1], [[1, 2, 13], 83], [[1, -1, 0], 0], [[14, 1], 83], [[1, 2, 3, 1], 1], [[1, 2, 13, 1], 1], [[3, 1, 2, 1, 2, 4], 3], [[4, 2, 1, 2, 8, 4, 1], 14], [[4, 1, 2, 3], 6], [[1, 2, 1], 8], [[2, 3], 0], [[4, 13, 1, 0], 6], [[1, 1], -1], [[], 2], [[2, 2], 2], [[3], -1], [[13, 83, 8], 0], [[2, 2, 2], 12], [[1, 13, 1, 0], 5], [[2], 13], [[1, 1, 1, 1, 1, 1], 7], [[0], 1], [[13, 2, 1], 3], [[1, 10, 1, 1], 4], [[48.77540799744989, -3.8838243003108204, -48.319352731351685], 2], [[2, 3, 2], -1], [[4, 1, 2, 8, 4], 13], [[13, 1], 2], [[48.77540799744989, -48.319352731351685, -3.8838243003108204, -48.319352731351685], 2], [[1, 2, 3], 5], [[1, 1, 0, 0], -15], [[1], 14], [[4, 1, 2, 3], 0], [[1, 10, 1, 1], 83], [[1, 2, 3, 2, 1], 8], [[12, 13, 83, 8], 0], [[7, 2, 2], 12], [[4, 2, 1, 2, 4, 4], 2], [[2, 3, 2], 1], [[3, 1, 2, 1, 2, 4, 2], 3], [[1, 2, 1, 1], 8], [[13, 83, 8], 1], [[4, 1, 13, 1, 0], 6], [[3], 14], [[1, 2, 13, 13], 12], [[14, 1], 82], [[6], -15], [[1, 13, 1, 0], 8], [[1, 1, 1, 1, 1, 1, 1, 1, 1], 7], [[1, 0], -1], [[7, 2], 12], [[4, 1, 2, 3], 1], [[2, 3, 2], -2], [[1, 1, 1, 1, 1], 7], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 20], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 20], [[1, 3, 5, 7, 9, 7, 5, 3, 1], 30], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 20], [[1, 2, 3, 4], 5], [[1, 2, 3, 2, 1, 0], 7], [[1, 2, 3, 4, 5, 6], 6], [[1, 2, 3, 2, 1], 6], [[7], 7], [[1, 2, 3, 2, 1, 0, 1], 7], [[2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12], 3], [[1, 2, 3, 1, 2, 1, 0, 1], 7], [[1, 2, 3, 2, 1, 0, 1], 8], [[1, 2, 3, 2, 1, 0, 1], 4], [[1, 2, 3, 2, 1, 0, 1, 1], 8], [[1, 2, 3, 4, 5, 6], 1], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1], 14], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 20], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1, 2], 14], [[1, 2, 3, 2, 1, 2, 2], 6], [[1, 3, 2, 1, 0], 8], [[1, 2, 2, 1, 0], 7], [[1, 3, 5, 7, 9, 7, 5, 3, 1], 1], [[2, 2, 1], 7], [[1, 5, 2, 3, 4, 5, 6], 1], [[1, 4, 2, 3, 2, 1, 1], 8], [[1, 3, 2, 1, 0, 1], 8], [[1, 4, 3, 3, 2, 1, 1], 8], [[14, 2, 3, 4, 5], 6], [[1, 2, 3, 4, 5, 6], 5], [[1, 3, 1, 5, 7, 9, 7, 5, 3, 1, 5], 8], [[1, 2, 3, 2, 1, 0, 2], 7], [[0, 2, 3, 2, 1, 0, 2], 7], [[1, 2, 3, 2, 1, 0, 1], 9], [[1, 2, 3, 2, 1, 0, 9, 1], 9], [[2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12], 3], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 21], [[1, 2, 1, 0], 8], [[14, 7], 8], [[1, 2, 3, 4, 5, 6], 4], [[4, 2, 3, 2, 1, 1], 8], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2], 20], [[1, 3, 5, 7, 9, 7, 5, 3, 1], 5], [[1, 2, 3, 2, 1, 0, 1, 1], 7], [[1, 2, 3, 4, 5, 3], 6], [[1, 2, 3, 5, 6], 1], [[1, 4, 2, 5, 3, 2, 1, 1], 8], [[1, 2, 3, 2, 1, 0, 1, 0, 2, 2], 8], [[1, 3, 5, 7, 9, 7, 5, 3, 1, 5], 7], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 1], [[1, 2, 1, 0], 14], [[1, 2, 3, 2, 1, 0, 1, 1], 4], [[2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12], 4], [[1, 2, 4, 1, 0], 14], [[2, 2, 1, 0], 21], [[2, 2, 1, 4], 21], [[1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 1], [[1, 2, 3, 4, 5, 6], 10], [[1, 7, 2, 3, 4, 5, 6], 6], [[1, 2, 3, 1, 2, 1, 0, 1], 10], [[1, 2, 3, 2, 1, 0, 9, 1], 0], [[2, 3, 2, 1], 8], [[30, 14, 2, 3, 4, 4, 5], 5], [[7, 7], 7], [[4, 2, 3, 2, 1, 1, 1], 0], [[2, 2, 18, 0], 30], [[1, 2, 3, 2, 1, 0, 9, 1, 1], 9], [[1, 4, 2, 5, 1, 3, 2, 1, 1], 8], [[2, 4, 6, 8, 10, 12, 16, 18, 20], 20], [[1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2], 20], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 17], [[2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12], 4], [[1, 4, 2, 5, 1, 14, 3, 2, 1, 1], 8], [[1, 2, 2, 1], 8], [[1, 3, 2, 1, 0], 7], [[1, 7, 2, 3, 4, 5, 6], 5], [[1, 2, 5, 3, 4, 5, 6], 4], [[2, 2, 18, 0], 31], [[1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16], 20], [[0, 1, 4, 2, 5, 1, 3, 2, 1, 1], 8], [[1, 2, 3, 4, 5, 6], 3], [[1, 2, 3, 2, 1, 0, 1, 1, 1], 4], [[2, 4, 6, 8, 10, 12, 16, 18, 20], 21], [[1, 2, 3, 2, 1, 0, 1, 1], 9], [[1, 1, 2, 3, 5, 6], 0], [[14, 2, 3, 4, 5, 5], 6], [[1, 2, 5, 3, 4, 5, 6], 6], [[0, 1, 2, 5, 1, 3, 2, 1, 1], 8], [[2, 3, 1, 2, 1, 0, 1], 7], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 7, 2, 2], 20], [[2, 1, 2, 3, 2, 1], 7], [[1, 4, 3, 3, 2, 1, 1, 1], 21], [[1, 2, 3, 2, 1, 0, 1, 0, 2, 2], 14], [[1, 2, 5, 3, 4, 5, 6, 5], 6], [[1, 2, 3, 7, 2, 1, 0, 1], 7], [[1, 2, 3, 1, 0, 1, 1], 1], [[3, 3, 3, 2, 1, 0, 1], 7], [[1, 4, 3, 3, 2, 1, 1], 9], [[1, 4, 2, 3, 2, 1, 1, 1], 8], [[1, 3, 2, 1, 0, 2], 8], [[1, 2, 30, 3, 2, 1, 0, 2], 7], [[14, 2, 3, 4, 5, 5], 7], [[1, 2, 3, 2, 1, 0, 12, 1, 1], 8], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 16], [[1, 2, 3, 4, 5, 6, 6], 7], [[2, 6, 8, 10, 16, 18, 31, 20], 20], [[1, 2, 3, 1, 2, 1, 0, 1], 30], [[1, 2, 3, 2, 1, 0, 1, 1], 31], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 19], [[1, 2, 3, 2, 1, 0, 1, 1, 1], 9], [[1, 4, 3, 3, 12, 1, 1, 1, 1], 7], [[0, 1, 2, 5, 1, 31, 3, 2, 1], 8], [[1, 2, 3, 2, 1, 0, 1], 31], [[1, 2, 2, 2, 1, 0, 2], 9], [[1, 2, 3, 2, 1, 0, 1], 14], [[1, 2, 4, 1, 0], 2], [[1, 2, 2, 1], 7], [[30, 14, 2, 4, 4, 5], 10], [[14, 2, 3, 4, 5, 3], 6], [[1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16], 1], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 20], [[1, 3, 5, 7, 9, 7, 3, 1, 5], 7], [[1, 30, 3, 1, 5, 7, 9, 7, 5, 3, 1, 5], 8], [[1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 21], [[2, 2, 1, 0], 20], [[1, 2, 3, 6, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 2], 20], [[2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12, 6], 3], [[1, 2, 3, 7, 2, 1, 0, 1], 6], [[1, 2, 3, 2, 1, 0, 1], 30], [[1, 2, 4, 5, 0], 14], [[1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 1], [[1, 2, 3, 2, 1, 0, 1], 12], [[2, 4, 6, 8, 10, 12, 16, 18, 20], 13], [[1, 4, 2, 3, 2, 1, 1, 1], 9], [[1, 2, 3, 2, 1, 0, 9, 1], 30], [[1, 4, 31, 3, 3, 2, 2, 1, 1, 1], 21], [[1, 5, 7, 9, 7, 5, 3, 1, 5], 7], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2], 21], [[1, 2, 5, 3, 4, 5, 6, 5, 5], 6], [[7, 2, 4, 5, 5], 6], [[1, 4, 2, 3, 2, 0, 1], 8], [[1, 4, 2, 5, 3, 2, 1], 8], [[2, 2, 1, 0, 2], 17], [[2, 4, 6, 8, 10, 14, 17, 17, 20, 12], 4], [[1, 2, 3, 2, 1, 0, 1, 1, 1], 1], [[2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12], 3], [[0, 1, 4, 2, 5, 1, 3, 2, 1, 1], 10], [[1, 5, 7, 9, 7, 5, 1, 5], 8], [[0, 2, 3, 2, 1, 0, 1, 1, 1], 31], [[2, 4, 6, 8, 10, 12, 14, 17, 17, 20, 12], 11], [[1, 5, 2, 3, 4, 5, 6], 2], [[2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 17], [[1, 2, 11, 4, 5, 6], 4], [[1, 4, 2, 5, 3, 2, 1, 1], 21], [[], 6], [[1, 3, 5, 7, 4, 9, 7, 5, 3, 1], -1], [[14, 2, 3, 4, 5, 3], 5], [[1, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 2], [[14, 2, 3, 4, 5, 18, 3], 6], [[1, 10, 3, 1, 2, 1, 0, 1], 30], [[30, 14, 4, 4, 5], 10], [[1, 3, 1, 0], 7], [[1, 2, 2, 1, 0], 6], [[1, 30, 3, 5, 7, 9, 7, 5, 3, 1, 5], 8], [[1, 5, 7, 10, 7, 5, 3, 1, 5], 7], [[1, 2, 3, 4, 5, 6], 9], [[1, 2, 1, 0], 6], [[1, 3, 18, 4, 1, 0], -1], [[2, 2, 18, 0], 13], [[1, 4, 2, 5, 3, 2, 1, 1], 9], [[1, 4, 31, 3, 3, 2, 2, 1, 1, 1], 9], [[1, 2, 3, 2, 1, 1, 0, 1, 1], 31], [[1, 2, 2, 3, 4, 5, 6], 5], [[1, 2, 4, 3, 4, 5, 7], 7], [[1, 2, 5, 3, 4, 5, 6], 1], [[2, 3, 2, 1, 0, 1], 9], [[2, 4, 6, 8, 10, 14, 17, 17, 20, 12, 10], 4], [[30, 14, 4, 4], 10], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3], 20], [[2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12], 2], [[1, 2, 3, 2, 1, 0, 1], 42], [[2, 4, 8, 10, 12, 14, 16, 18, 21], 20], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 22], [[1, 2, 11, 4, 5, 6], 10], [[1, 2, 3, 2, 1, 0, 1, 21, 3], 2], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2], 13], [[1, 2, -1, 4, 5, 0], 13], [[1, 4, 3, 4, 5, 6], 6], [[1, 2, 31, 1, -1, 0], 6], [[1, 2, 3, 8, 2, 1, 0, 1], 7], [[14, 2, 4, 5, 3], 6], [[2, 2, 1, 4], 12], [[2, 2, 1], 8], [[1, 2, 3, 1, 2, 1, 0, 1, 2], 30], [[1, 4, 3, 3, 2, 1, 1, 1], 8], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 19], [[2, 1, 0], 22], [[2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12], 30], [[1, 2, 4, 5, 6], 6], [[1, 4, 3, 3, 2, 1, 1, 4], 2], [[1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 2, 2], 19], [[1, 2, 1, 0, 0], 14], [[1, 2, 5, 3, 4, 5, 6], 20], [[4, 2, 3, 2, 0], 8], [[1, 3, 5, 7, 4, 9, 7, 5, 1], -1], [[30, 14, 2, 4, 5], 10], [[1, 4, 2, 3, 2, 0, 1], 0], [[1, 2, 5, 3, 4, 4, 6, 5], 6], [[0, 1, 9, 2, 5, 1, 3, 2, 1, 1], 8], [[1, 2, 2, 1, 2, 3, 2, 2, 2, 3, 2, 2, 2], 17], [[30, 14, 2, 3, 4, 4, 5], 6], [[2, 4, 11, 6, 8, 10, 12, 14, 17, 18, 20, 12, 6], 3], [[1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 21], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2], 22], [[2, 3, 2, 1], 7], [[1, 4, 3, 3, 1, 1, 1, 1], 21], [[0, 5, 1, 2, 0, 4, 5, 6], 5], [[1, 5, 3, 5, 6, 5], 6], [[1, 2, 1], 14], [[1, 2, 3, 4], 21], [[4, 2, 3, 2, 0, 2], 8], [[1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2], 6], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3], 16], [[1, 2, 3, 2, 1, 0, 1, 1], 16], [[2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12], 9], [[1, 2, 1, 3, 2, 1, 0], 7], [[1, 2, 3, 4, 6], 9], [[0, 1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 2, 16], 1], [[1, 1, 2, 3, 1, 0, 1, 1], 1], [[1, 2, 2, 1, 0, 1], 7], [[1, 2, 3, 1, 2, 1, 0, 1, 2], 7], [[1, 2, 9, 3, 2, 1, 0, 9, 1], 22], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2], 30], [[1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3], 1], [[1, 3, 2, 1, 2, 2], 6], [[1, 3, -1, 4, 5, 0], 13], [[1, 4, 3, 3, 2, 1, 1], 7], [[14, 2, 4, 5, 3, 3], 6], [[14, 2, 3, 4, 5, 3], 16], [[1, 2, 3, 2, 1, 0, 1, 1, 1], 31], [[2, 2, 1, 4], 6], [[7], 6], [[2, 3, 2, 1], 0], [[1, 2, 3, 21, 5, 6, 4], 14], [[2, 4, 6, 8, 10, 14, 17, 17, 20, 12, 8], 10], [[1, 2, 4, 1, 0, 4], 14], [[1, 2, 3, 2, 1, 2], 6], [[1, 2, 4, 5, 0], 15], [[1, 2, 3, -1, 2, 1, 2, 0, 1], 4], [[1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 1, 16], 31], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 20, 2, 3, 2, 2, 3, 3], 16], [[1, 4, 3, 3, 12, 1, 1, 1, 1], 6], [[1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 4, 2, 1, 7, 2, 2], 19], [[7], 8], [[1, 2, 2, 3, 2, 1, 0], 7], [[0, 1, 2, 5, 1, 31, 3, 2, 1], 13], [[0, 1, 15, 5, 1, 3, 2, 1, 1], 8], [[6, 8, 10, 16, 19, 31, 20], 20], [[1, 2, 3, 2, 1, 0, 14], 16], [[1, 2, 5, 3, 4, 4, 6, 5, 3], 6], [[1, 2, 3, 1, 2, 1, 0], 9], [[1, 2, 42, 3, 4], 5], [[1, 3, 2, 1, 1, 2], 6], [[2, 3, 2, 1, 0], 21], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 22], 19], [[1, 2, 3, 2, 1, 0, 1, 1, 2, 1], 15], [[1, 6, 3, 5, 7, 9, 7, 5, 3, 1], 17], [[1, 4, 3, 4, 5, 6], 13], [[1, 1, 2, 1, 2, 3, 2, 1, 2, 2, 2, 3], 15], [[30, 14, 4, 4, 4], 10], [[2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12, 12], 4], [[6, 8, 10, 16, 19, 31, 20, 20], 42], [[2, 4, 6, 8, 10, 12, 14, 7, 17, 18, 20, 12, 6], 3], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3, 3, 3], 20], [[2, 2, 1, 1, 0], 20], [[14, 2, 3, 4, 5, 3], 4], [[1, 4, 3, 3, 2, 1, 1], 10], [[4, 2, 3, 2, 0, 2, 2], 8], [[1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 2, 3], 1], [[2, 3, 1, 4, 5, 6], 0], [[1, 2, 1, 1, 2], 6], [[1, 2, 2, 3, 1, 0], 7], [[1, 2, 3, 2, 1, 0, 1, 1, 1], 19], [[1, 7, 2, 3, 4, 5, 6], 16], [[1, 5, 7, 21, 7, 5, 1, 5], 7], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 11, 2, 3, 2, 1, 7, 2, 2], 20], [[1, 2, 3, 2, 1, 0, 9, 1], 22], [[30, 14, 4, 4, 4, 4], 16], [[2, 2, 1, 0, 2, 2], 0], [[1, 5, 7, 9, 7, 5, 3, 1, 5, 5], 7], [[1, 3, 2, 2, 1, 1, 2, 1], 6], [[10, 2, 2, 1, 0, 2], 17], [[1, 3, 5, 7, 9, 7, 5, 3, 1, 7], 30], [[1, 1, 7, 2, 3, 4, 5, 6], 4], [[13, 2, 3, 4, 5, 3], 4], [[1, 3, 2, 2, 1, 1, 2, 1, 1], 6], [[1, 31, 1, 2, 3, 1, 0, 1, 1], 1], [[1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 3, 2], 19], [[1, 2, 3, 1, 2, 1, 2, 3, 2, 2, 1, 2, 3, 2, 2], 20], [[3, 3, 2, 1, 1, 1], 21], [[1, 2, 30, 3, 1, 0, 1, 1, 1], 2], [[2, 2, 18, 0], 29], [[1, 2, 2, 3, 4, 5, 6, 2], 5], [[1, 2, 2, 3, 2, 1, 2, 3, 1, 2, 3, 2, 1], 21], [[1, 10, 31, 3, 1, 2, 1, 0, 1], 30], [[7, 1, 2, 1, 0, 0], 14], [[2, 1, 2, 3, -1, 2, 1, 2, 0, 1], 4], [[2, 3, 1, 4, 5, 6], -1], [[1, 2, 3, 2, 1, 0, 1, 1, 0], 4], [[2, 3, 2, 1, 0, 1], 8], [[1, 2, 4, 5, 6], 9], [[1, 3, 2, 2, 1, 1, 2, 1, 1], 5], [[1, 7, 2, 3, 4, 5, 6], -1], [[1, 2, 3, 2, 1, 0, 9, 1, 3], 22], [[1, 3, 18, 16, 7, 0], -1], [[2, 2, 4], 6], [[1, 2, 15, 3, 2, 1, 0, 1], 7], [[1, 2, 3, 5, 6, 1], 20], [[2, 4, 6, 8, 17, 10, 12, 13, 17, 20, 12], 2], [[1, 4, 2, 5, 2, 1, 1], 9], [[1, 4, 2, 5, 1, 3, 3, 2, 1, 1], 8], [[2, 2, 4], -1], [[1, 29, 1, 2, 1, 0, 4, 1], 7], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2], 19], [[1, 2, 3, 5, 6], 5], [[1, 2, 3, 3, 1, 2, 3, 2, 2, 3, 2, 16], 20], [[1, 2, 3, 2, 2, 3, 2, 1, 2, 3, 2, 2, 2], 22], [[1, 3, 2, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 2, 2], 7], [[1, 2, 3, 2, 20, 2, 3, 2, 1, 1, 3, 2, 3, 2, 1, 7, 2, 2], 20], [[1, 2, 3, 6, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2], 20], [[1, 3, 5, 7, 9, 7, 5, 3, 1, 3], 6], [[4, 2, 3, 1, 1, 1], 0], [[4, 2, 3, 2, 0, 2], 9], [[13, 3, 4, 5, 3, 3], 42], [[1, 2, 1, 2, 1, 2, 3, 1, 2, 3, 2, 3], 1], [[1, 2, 3, 1, 2, 3, 2, 2, 3, 2, 16], 13], [[1, 2, 3, 2, 1, 3], 29], [[1, 2, 3, 2, 1, 0, 1], 5], [[2, 4, 6, 8, 10, 12, 13, 17, 20, 12], 2], [[1, 4, 2, 5, 3, 2, 1, 2], 20], [[1, 29, 1, 2, 1, 17, 4, 1], 7], [[1, 2, 1, 3, 2, 1, 0, 9, 1], 30], [[1, 4, 2, 5, 1, 3, 3, 2, 1], 8], [[2, 2, 1, 0, 2, 2], 30], [[1, 2, 3, 2, 1, 0, 1, 0, 2, 2], 20], [[1, 2, 3, 1, 2, 1, 16, 3, 2, 1, 2, 3, 2, 2], 20], [[1, 2, 4, 2, 3, 2, 0, 1], 0], [[1, 31, 1, 2, 3, 1, 1, 1], 1], [[3, 3, 2, 1, 1, 1, 1], 10], [[1, 4, 3, 3, 2, 1, 1, 4], 31], [[1, 4, 2, 3, 2, 0, 1, 2], 8], [[3, 3, 3, 2, 1, 0, 7], 7], [[30, 14, 4, 4, 4, 4], 6], [[1, 4, 3, 4, 5, 6], 8], [[1, 2, 4, 5, 6], 4], [[2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 20, 12], 22], [[1, 2, 3, 2, 1, 1, 0, 9, 1], 31], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 21], [[1, 2, 3, 3, 1, 1, 2, 3, 2, 1, 2, 3, 2, 16], 20], [[6, 8, 10, 19, 3, 31, 20], 20], [[6, 16, 8, 10, 19, 3, 31, 20], 20], [[1, 2, 1, 1, 3, 2, 1, 0], 7], [[1, 0, 2, 5, 3, 4, 5, 6], 20], [[1, 3, 2, 2, 1, 1, 2, 1, 1, 1], 5], [[17, 3, 1, 4, 5, 6], -1], [[1, 5, 7, 9, 7, 5, 1, 5], 16], [[1, 30, 5, 7, 9, 7, 5, 3, 1, 5], 29], [[13, 3, 4, 5, 3], 13], [[2, 5, 2, 1], 4], [[2, 4, 6, 8, 10, 12, 14, 17, 18, 20, 12], 4], [[1, 2, 3, 2, 2, 3, 2, 1, 2, 2, 2, 2], 22], [[1, 7, 3, 5, 7, 9, 7, 5, 3, 1], 7], [[7, 2, 5, 5, 5], 6], [[1, 31, 3, 2, 1, 0, 1], 18], [[2, 4, 5, 8, 10, 12, 16, 18, 20], 13], [[7], 21], [[2, 2, 18, 0], 7], [[1, 5, 3, 6, 5, 1], 5], [[1, 3, 5, 7, 4, 9, 7, 5, 1], 42], [[1, 1, 2, 3, 5, 6, 3], 0], [[15, 3, -1, 4, 5, 0], 13], [[1, 2, 3, 2, 1, -1, 1], 7], [[1, 14, 3, 4, 1], 4], [[2, 5, 3, 4, 5, 6], 6], [[2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 2], 21], [[14, 3, 1, 0], 7], [[30, 14, 4, 5, 4], 10], [[0, 1, 15, 5, 1, 3, 2, 1, 0], 8], [[1, 3, 5, 7, 9, 7, 5, 3, 1], 29], [[1, 2, 2, 0, 1, 0], 6], [[2, 2, 18, 1, 0], 29], [[1, 2, 5, 3, 4, 5, 6, 5], 21], [[4, 2, 3, 2, 0, 2], 12], [[30, 2, 3, 4, 5, 3], 6], [[1, 4, 2, 5, 3, 2, 1, 1], 22], [[1, 2, 5, 6], 31], [[1, 2, 31, 1, 0], 16], [[1, 2, 2, 3, 1, 0], 8], [[1, 4, 2, 5, 3, 2, 1, 2, 2], 21], [[1, 2, 3, 1, 2, 13, 1, 0, 1], 30], [[1, 5, 7, 9, 7, 5, 3, 1, 5, 5, 1], 7], [[1, 2, 1, 1, 3, 2, 1, 0], 8], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1, 16], 31], [[30, 14, 4, 4, 5, 30], 10], [[3, 4, 16, 6, 10, 14, 17, 17, 20, 12], 4], [[1, 3, 2, 5, 7, 9, 7, 5, 3, 13, 1, 5], 9], [[1, 2, 5, 3, 4, 4, 6, 5, 3], 10], [[1, 2, 3, 5, 6, 5], 20], [[1, 5, 7, 9, 7, 5, 1, 5], 5], [[1, 5, 2, 4, 5, 6], 9], [[1, 2, 3, 1, 2, 3, 2, 2, 3, 2, 16], 4], [[1, 2, 3, 2, 1, 2, 3, 2, 30, 1, 3, 2, 3, 2, 1, 7, 3, 2], 18], [[1, 30, 3, 7, 9, 7, 5, 3, 1, 5], 8], [[4, 7, 3, 2, 1, 1, 1], 0], [[7, 1, 2, 1, 0, 0, 0], 30], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 3], 1], [[2, 2, 1, 0, 2, 18], 0], [[1, 4, 2, 5, 3, 2, 1, 1], 15], [[1, 2, 3, 2, 1, -1], 8], [[7, 2, 5, 5, 5, 5], 1], [[1, 2, 2, 1, 3], 29], [[1, 4, 2, 1, 1, 3, 2, 1, 0], 4], [[1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1], 21], [[6, 8, 10, 16, 19, 31, 20], 15], [[1, 2, 3, 5, 6, 1], 19], [[1, 2, 3, 2, 1, 0, 1, 1], 17], [[2, 4, 5, 8, 10, 12, 16, 18, 20], 15], [[14, 2, 3, 4, 5, 5], 5], [[1, 2, 2, 3, 4, 5, 6, 2], 4], [[1, 2, 3, 2, 1, 0, 1, 1, 0, 1], 4], [[0, 1, 2, 5, 1, 31, 3, 2, 1, 31], 8], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 6, 1, 2, 2], 14], [[1, 2, 3, 6, 2, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2], 4], [[1, 2, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 1, 2], 14], [[1, 2, 15, 3, 2, 1, 0, 1], 8], [[1, 2, 3, 2, 1, 13, 1], 30], [[2, 3, 1, 4, 5, 6, 2], -1], [[1, 2, 4, 7, 0], 15], [[1, 4, 3, 3, 3, 2, 1, 1], 9], [[2, 2, 18, 19, 0], 42], [[1, 4, 2, 5, 2, 2, 1, 1], 15], [[1, 3, 18, 16, 7, 0, 16], 9], [[1, 2, 2, 1, 0, 1], 22], [[1, 30, 3, 7, 9, 7, 5, 3, 5], 8], [[1, 2, 3, 3, 1, 2, 3, 1, 2, 3, 2, 16], 1], [[1, 2, 5, 1, 3, 2, 1, 1], 3], [[1, 2, 2, 1, 0, 2], 7], [[1, 2, 2, 3, 1, 0], 18], [[2, 1, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], -1], [[2, 4, 8, 10, 12, 14, 16, 18, 21, 16], 20], [[14, 2, 4, 5, 5, 3], 3], [[4, 2, 3, 2, 1, 1, 1], 42], [[10, 2, 2, 1, 0, 2], 11], [[1, 4, 3, 3, 4, 29, 2, 1, 1], 9], [[4, 2, 3, 1, 1, 1], 12], [[1, 3, 5, 7, 9, 7, 5, 3, 1], 7], [[1, 2, 3, 2, 1, 2], 7], [[2, 6, 4, 6, 8, 10, 12, 16, 18, 20], 20], [[1, 2, 1, 1, 3, 2, 5, 1, 0], 7], [[1, 2, 5, 3, 4, 5, 6, -1], 6], [[14, 2, 3, 4, 5, 3], 31], [[1, 15, 2, 11, 2, 1, -1], 20], [[1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 3, 1, 16, 3], 31], [[1, 4, 4, 4, 5, 6], 19], [[1, 7, 2, 3, 4, 5, 6], 22], [[20, 2, 4, 6, 8, 10, 12, 13, 17, 17, 20, 12, 2], 4], [[1, 2, 30, 2, 1, 0, 1, 0, 2, 2], 20], [[2, 2, 1, 1, 0], 19], [[2, 5, 6, 8, 10, 30, 14, 17, 17, 20, 12, 10], 4], [[2, 2, 0, 2, 18], 12], [[0, 1, 2, 5, 1, 31, 3, 2, 1, 31, 2], 8], [[1, 3, 7, 2, 0, 1], 7], [[1, 2, 3, 2, 1, 2, 2], 17], [[1, 2, 3, 1, 2, 1, 0], 19], [[1, 2, 3, 2, 1, 0, 1, 0, 1], 0], [[2, 6, 18, 8, 10, 16, 18, 31, 20], 20], [[1, 1, 2, 3, 2, 1, -1, 1], 9], [[1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 1, 4], -1], [[7, 2, 4, 5, 5, 2], 16], [[4, 2, 3, 2, 0, 1, 2], 8], [[19, 4, 8, 10, 12, 14, 16, 18, 21, 16], 20], [[6, 3, 3, 2, 1, 0, 1], 7], [[30, 14, 15, 4, 4, 5], 10], [[1, 3, 5, 7, 9, 7, 5, 3, 1, 3, 5], 6], [[2, 4, 6, 8, 10, 12, 14, 17, 17, 20], 4], [[2, 4, 6, 8, 10, 12, 14, 17, 18, 12], 22], [[1, 2, 3, 2, 1, 0, 1, 1, 2, 1], 5], [[1, 31, 1, 2, 3, 1, 0, 1, 1, 2], 1], [[1, 3, 2, 1, 2, 2], 17], [[14, 2, 4, 5, 3, 3, 3], 6], [[1, 2, 3, 2, 1, 0, 9, 1], 1], [[1, 6, 2, 3, 4, 5, 6, 2], 4], [[1, 3, 2, 1, 1, 2], 7], [[4, 1, 3, 2, 1, 0], 8], [[3, 3, 3, 15, 1, 0, 1], 7], [[1, 2, 2, 3, 2, 1, 0], 9], [[1, 4, 2, 5, 3, 2, 1], 7], [[2, 4, 6, 8, 10, 12, 14, 11, 17, 17, 10, 20, 12], 22], [[7, 2, 5, 5, 5], 1], [[1, 2, 17, 1, 2, 1, 16, 3, 2, 1, 2, 3, 2, 2], 20], [[1, 2, 3, 2, 1, 0, 1], 15], [[2, 5, 2, 1, 0, 2, 2, 2, 2], 0], [[0, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 3, 2], 1], [[1, 2, 3, 3, 1, 2, 3, 2, 1, 2, 9, 1, 16, 1], 31], [[1, 3, 18, 16, 7, 12, 16, 16], 9], [[1, 31, 1, 2, 3, 1, 1, 1], 0], [[], 10], [[], 8], [[3], 0], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 100], [[10], 5], [[], 1], [[2], 1], [[2], 3], [[2, 5, 2], 10], [[1, 2, 3, 4], 8], [[1, 3, 5, 4, 7, 9, 7, 5, 3, 1, 5], 6], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 2], 19], [[1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2], 20], [[1, 2, 3, 2, 1, 0, 0, 0], 7], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 18], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 19], [[1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2], 0], [[1, 2, 3, 1], 5], [[1, 2, 3, 2, 1, 0], 8], [[1, 10, 2, 4, 3, 2, 1, 4], 7], [[1, 1, 2, 3], 1], [[4, 6, 8, 10, 12, 14, 16, 18, 20], 20], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 19], [[1, 2, 14, 4], 5], [[1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 4, 3, 2, 2], 20], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 2, 2], 3], [[1, 2, 3, 4], 9], [[1, 2, 3, 2, 1, 14, 3, 2, 1, 2, 3, 2, 2], 20], [[1, 2, 4], 5], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1], 20], [[1, 2, 3, 4, 4], 5], [[30, 2, 3, 4, 4], 5], [[1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1], 6], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1], 19], [[2, 3, 2, 1, 0], 8], [[1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2, 2], 0], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 14], 20], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1], 19], [[30, 2, 3, 4, 4], 12], [[1, 3, 5, 7, 4, 9, 7, 5, 3, 1], 30], [[4, 6, 8, 10, 12, 14, 16, 18, 20], 7], [[6, 1, 3, 5, 4, 7, 9, 7, 5, 3, 1, 5], 6], [[30, 3, 3, 4, 4], 12], [[1, 3], 5], [[1, 2, 3, 2, 1, 2, 18, 3, 2, 1, 4, 3, 2, 2], 20], [[30, 2, 3, 2, 4, 4], 5], [[8, 1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5], 30], [[30, 3, 3, 4, 4], 11], [[30, 2, 3, 2, 4, 4], 4], [[1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1], 12], [[1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5], 30], [[1, 3], 7], [[4, 6, 8, 10, 12, 14, 16, 18, 20], 5], [[30, 12, 2, 3, 2, 4, 4], 0], [[1, 2, 3, 4, 5, 6, 2], 6], [[1, 2, 3, 4, 5, 6], 7], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2], 0], [[1, 2, 3, 2, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2], 20], [[1, 1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 1], 19], [[4, 6, 8, 10, 12, 14, 18, 11], 5], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 1], 19], [[1, 3, 4, 5, 6, 2], 19], [[1, 2, 3, 2, 1, 18, 3, 3, 2, 1, 2, 3, 2, 2], 21], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1, 3], 19], [[1, 5, 7, 9, 7, 5, 3, 1], 30], [[1, 2, 3, 2, 1, 2, 3, 3, 2, 1, 2, 4, 2, 2], -1], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 9], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 1], 31], [[1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3], 6], [[1, 3, 4, 5, 6, 2], 20], [[30, 3, 3, 4, 4], 18], [[1, 8, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 7], [[1, 2, 2, 1, 2, 3, 2, 1, 2, 19, 2, 3], 3], [[1, 3], 4], [[1, 1, 8, 2, 3, 2, 1, 3, 2, 1, 2, 3, 2, 1], 6], [[4, 6, 8, 10, 12, 14, 16, 18, 20, 12], 19], [[1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 2, 2], 0], [[1, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1], 19], [[1, 2, 3, 2, 30], 14], [[1, 3, 4, 5, 6, 2], 21], [[1, 3, 5, 7, 4, 9, 7, 5, 3, 1, 5], 9], [[30, 2, 3, 2, 4, 4], 12], [[1, 14], 7], [[1, 2, 3, 2, 7, 2, 3, 2, 1, 2, 2, 2, 2], 12], [[1, 8, 2, 3, 2, 1, 3, 2, 2, 1, 2, 3, 2, 1], 12]]
    results = [True, False, True, False, False, True, True, True, True, False, True, False, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(will_it_fly)