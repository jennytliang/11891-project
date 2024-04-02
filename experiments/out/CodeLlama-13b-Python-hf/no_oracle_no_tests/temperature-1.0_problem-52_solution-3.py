def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True


def all_above_threshold(l: list, t: int):
    """Return True if all numbers in the list l are above threshold t.
    >>> all_above_threshold([1, 2, 4, 10], 5)
    False
    >>> all_above_threshold([1, 20, 4, 10], 5)
    True
    """
    for i in l:
        if i <= t:
            return False
    return True


def any_above_threshold(l: list, t: int):
    """Return True if any number in the list l is above threshold t.
    >>> any_above_threshold([1, 2, 4, 10], 5)
    True
    >>> any_above_threshold([1, 20, 4, 10], 5)
    True
    >>> any_above_threshold([1, 2, 4, 10], 20)
    False
    """
    for i in l:
        if i > t:
            return True
    return False


def all_below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> all_below_threshold([1, 2, 4, 10], 100)
    True
    >>> all_below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True


def all_equal(l: list):
    """Return True if all numbers in the list l are equal.
    >>> all_equal([1, 1, 1, 1])
    True
    >>> all_equal([1, 2, 3, 4])
    False
    >>> all_equal([1, 1, 1, 1, 2])
    False
    """
    for i in l:
        if i != l[0]:
            return False
    return True


def run_tests():
    import doctest
    doctest.testmod(verbose=True)


def main():
    run_tests()


if __name__ == "__main__":
    main()




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
    inputs = [[[1, 2, 4, 10], 100], [[1, 20, 4, 10], 5], [[1, 20, 4, 10], 21], [[1, 20, 4, 10], 22], [[1, 8, 4, 10], 11], [[1, 8, 4, 10], 10], [[0, 0, 0, 0], 1], [[1, 3, 5, 7], 10], [[-1, -2, -3, -4], 0], [[2, 4, 6, 8], 7], [[], 5], [[1, 2, 3, 4], 4], [[-4, -3, -2, -1], -5], [[1, 2, 4, 10], 0], [[1, 4, 7, 10], 6], [[3.5, 2.2, 1.1], 5], [[1, 3, 4], 4], [[1, 4, 7, 10], -2], [[1, 4, -4, 7, 10], 6], [[1, 2, 3, -1, 4], 4], [[1, 3, 5, 7, 5], 10], [[4, -4, 7, 10], 6], [[-4, -3, -2, -1], -1], [[1, 4, 7, 10, 7], 6], [[-4, -3, -2, 4, -4], -1], [[1, 2, 3, -1, 4], 5], [[1, 3, 5, 7], 11], [[0, -1, 0, 0, 0], 0], [[1, 4, 7, 9], 10], [[1, 2, -4, 4], 4], [[True, False], 5], [[-1, -2, -4], 0], [[True, False], 4], [[1, 3, 7, 5], 10], [[1, 2, 3, -1, 4, 4], 4], [[1, 3, 10, 4], 5], [[3, 1, 4, 7, 10, 7], 6], [[1.1, 3.5, 2.2, 1.1], 5], [[-4, -3, 4, -4], -1], [[1, 4, 7, 9, 1], 10], [[1, 4, 7, 10, 7], 5], [[3.5, 2.6445924145352944, 2.2, 1.1], 3], [[0, -1, -2, -4], 0], [[1, 3, 7, 5], -3], [[0, 0, 2, 0, 0], 1], [[-1, -2, -4], -4], [[True, False, False], 3], [[1, 3, 7, 5], -1], [[4, -4, 7, 10], -2], [[1, 4, 7, 9], 6], [[7, -2, -3, -3, -4], 0], [[True, False, False], -4], [[3.5, 2.2, 1.1], -4], [[-4, -3, -2, 4], -1], [[1, 2, 3, 4], 1], [[4, -4, 7, 10], 7], [[0, -1, 0, 0, 0], 8], [[1, 2, 5, 3, 4], 4], [[-1, 8, -2, -4, 8], -2], [[1, 3, 7, 5], 8], [[-1, -2, -4], -5], [[2, 4, 6, 8], 6], [[-3, -2, 4], -1], [[1, 4, 7, 9, 1], 11], [[1, 4, 7, 9, 9], 10], [[-2, -4], -4], [[1, 5, 7], 10], [[4, -4, 7, 10, -4], 7], [[1, 3, 4], 2], [[1, -3, 2, 3, 4], 1], [[6, 4, -4, 7, 10], 7], [[3.5, 2.2, 3.5], 5], [[1, 2, -5, -4, 4], 4], [[1, 3, 7, 5], 9], [[-2, -4], -5], [[1, 4, 7, 10, 7], 4], [[True, False, False], 5], [[1, 3, 7, 11], -3], [[-1, 8, -2, 8], -2], [[1, 0, 2, 0, 0], 2], [[-3, -3, -2, 4], -1], [[3.5, 3.5, 2.2, 3.5, 3.5], 5], [[4, -4, -2, 7, 10], 6], [[1, 0, 2, 0, 0], 3], [[1, 2, 3, -1, 4, 4], 5], [[1, 3, 7, 5, 3], 9], [[1, 8, 7, 5], -3], [[-2, -3, -3, -4], 0], [[-3, -2, 4, 4, -2], 0], [[-1, 1, 2, 3, -1, 4, 4], 4], [[3, 5, 7], 11], [[-4, -3, -2, 4], 0], [[-3, -2, 4], 8], [[False, True, False], 4], [[1, 2, -5, -4, 4], 11], [[-4, -3, -2, 4, -2], 1], [[3, 1, 1, 4, 7, 10, 7], 6], [[True, True, True], 4], [[5.5, 6.2, 7.9, 8.1], 9], [[10, 20, -30, 40, -50], 15], [[100, -200, 300, -400, 500, -600], 100], [[1000, 500, 250, 125, 62.5, 31.25], 2000], [[10000000, 9000000, 8000000, 7000000, 6000000, 2000000], 10000001], [[100, 200, 300, 0.1, 0.2, 0.3], 0], [[], 0], [[10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000], 10000001], [[2000000, 10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000], 10000001], [[], -1], [[10000000, 9000000, 8000001, 8000000, 7000000, 6000000, 2000000], 10000001], [[], 1], [[10, 20, -30, 40, -50], 20], [[1000, 500, 250, 125, 62.5, 31.25], 125], [[100, -200, 300, -400, 500, -600], 1], [[5.5, 6.2, 7.9, 8.1], 500], [[100, 2000000, 300, -400, 500, -600], 100], [[10000000, 9000000, 8000000, 7000000, 6000000, -200, 10000000], 10000001], [[10, 20, -30, 40, -50], 14], [[100, -200, -400, 500, -600], 8000001], [[5.5, 6.2, 7.9, 8.1], 501], [[2000000, 10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000, 7000000], 10000001], [[5.5, 6.2, 7.9, 8.1], 10], [[2000000, 10000000, 9000000, 10, 8000000, 6000000, 2000000, 8000000], 10000001], [[], 7000000], [[5.5, 6.2, 7.9, 8.1, 6.2], 10], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000], 10000001], [[5.5, 6.2, 7.9, 8.1, 6.2, 6.2], 10], [[62.5, 16.953176162073675, 2.9851560365316985], 1], [[2000000, 8000001, 10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000], 10000001], [[100, 2000000, 300, -400, 500, -600], -1], [[10000000, 9000000, 8000000, 7000000, 6000000, -200, 10000000], 10000002], [[0.1, 5.5, 6.2, 7.9, 8.1], 500], [[5.5, 6.2, 7.9, 8.1], 100], [[10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000], 10000002], [[10000000, 9000000, 8000001, 8000000, 7000000, 6000000, 2000000, 7000000], 125], [[2000000, 10000000, 9000000, 10, 8000000, 6000000, 2000000, 8000000], 10000002], [[100, -200, -400, 500, -600], 8000002], [[5.5, 6.2, 7.9, 8.565673083320917], 10], [[10, 20, -30, 40, -50], 499], [[10, 20, 21, -30, 40, -50], 15], [[100, 2000000, 300, 500, -600], 8000000], [[2000000, 10000000, 9000000, 10, 200, 7000000, 6000000, 2000000], 10000000], [[1000, 500, 250, 125, 62.5, 31.25], 1999], [[5.5, 6.2, 8.565673083320917], 10], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000], 10], [[100, 250, 2000000, 300, -400, 500, -600], 100], [[5.5, 6.2, 7.9, 8.1, 5.6573184258702085, 6.2], 10], [[5.5, 6.2, 7.9, 6.287047990560678, 8.1], 10000000], [[62.5, 16.953176162073675, 2.9851560365316985, 16.953176162073675], 1], [[2000000, 10000000, 9000000, 10, 8000000, 6000000, 2000000, 8000000], 10000003], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000], 10000001], [[10, 20, 1, 40, -50], 15], [[2000000, 8000001, 10000000, 9000000, 10, 8000000, 7000000, 2000000, 6000000, 2000000], 10000001], [[2000000, 8000001, 10000000, 9000000, 10, 8000000, 7000000, 2000000, 6000000, 2000000, 2000000], 10000001], [[], 1000], [[2000000, 8000001, 1000, 10000000, 9000000, 10, 8000000, 2000000, 6000000, 2000000, 2000000], 499], [[10, 20, -30, 40, 499], 14], [[5.5, 7.9, 8.1], 9], [[], -2], [[10, 20, -30, 40, -50], 19], [[100, 250, 2000000, 300, -400, 500, -600], 1999], [[1000, 500, 126, 250, 125, 62.5, 31.25, 31.25, 500], 2000], [[7.468707181862638, 5.5, 6.2, 7.9, 8.565673083320917], 10], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000], -50], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000, 10000001], 10], [[10, 20, -30, 40, -50], 13], [[100, -200, 300, -400, 500], 1], [[5.5, 6.2, 8.565673083320917, 6.2], 10], [[], 1001], [[10000000, 9000000, 8000000, 7000000, 6000000, 2000000], 8000002], [[10, 20, 21, -30, 40, -50], 14], [[100, 200, 300, 0.1, 0.2], 0], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000, 10000001], 0], [[100, 200, 300, 0.1, 0.2], 9000000], [[-200, 10, 20, -30, 40, -50], 8000000], [[10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000], 100], [[5.5, 6.2, 7.9], 11], [[16.953176162073675, 2.9851560365316985], 1], [[100, -200, 300, -400, 500, 300], 1], [[-200, 300, -400, 500, -600], 100], [[10, 20, -30, 40, -50, 20], 499], [[10, 20, -30, 40, 20, -50], 19], [[5.5, 2.8, 6.2, 8.1], 9], [[0.1, 5.5, 7.9, 8.1], 500], [[100, -200, 300, -400, 500, 499, -600], 1], [[10, 20, 1, 40, 9, -50, -50], 499], [[100, -200, 300, 0, 500, 300], 9], [[2000000, 9000000, 8000000, 6000000, 2000000, 8000000], -51], [[-200, 300, -400, -600, 300], 100], [[5.5, 6.2, 7.9, 8.1, 6.2, 6.2], 8000001], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000, 10000001], 8000001], [[5.5, 2.8, 6.2, 8.1], 7000001], [[-200, 300, 8000000, -400, -600, 300], 100], [[5.5, 6.2, 7.9], 13], [[1000, 500, 250, 125, 6.635714530100879, 62.5, 31.25], 2000000], [[100, 250, 2000000, 300, -400, 500, -600], 1998], [[10000000, 9000000, 1998, 8000000, 7000000, 6000000, 2000000], 100], [[100, 2000000, 300, -400, 500, -600], -2], [[5.5, 6.2, 7.9, 8.1, 5.6573184258702085, 6.2, 7.9], 10], [[1.5, 1000, 500, 250, 125, 6.635714530100879, 62.5, 31.25], 2000000], [[2000000, 10000000, 9000000, 10, 8000000, 7000000, 6000000, 1001, 2000000, 7000000], 10000000], [[10000000, 8000002, 9000000, 8000001, 8000000, 7000000, 6000000, 2000000, 7000000], 125], [[10, 20, 1, 40, 9, -50, -50], 500], [[2000000, 10000000, 9000000, 10, 8000000, 6000000, 2000, 8000000], -199], [[-200, 300, 8000000, -400, -600, 300], 1001], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000, 8000000], 10000001], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000], 200], [[100, -200, 300, -400, 500, 499, -600], 10000001], [[10, 20, 21, 300, -30, 40, -50, 10], 10], [[100, -200, -400, 500, -600], 10], [[9.263975784000001, 5.5, 6.2, 8.565673083320917, 6.2], 10], [[5.5, 2.8, 6.2, 8.1], 10000001], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000], 9999999], [[2000000, 10000000, 9000000, 10, 8000000, 6000000, 2000000, 8000000, 2000000], 10000001], [[100, 200, 300, 0.1, 0.2, 0.3, 0.2], -1], [[5.5, 6.2, 3.18463343128131, 7.9, 8.1, 5.6573184258702085, 6.2], 10], [[100, -400, 499, -600], 8000001], [[8000001, 10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000], 10000001], [[2000000, 10000000, 9000000, 10, 8000000, 6000000, 2000, 8000000], 7000001], [[10, -400, 20, -30, 40, 499], 40], [[8000001, 9999998, 10000000, 9000000, 10, 9999999, 8000000, 7000000, 6000000, 2000000], 10000001], [[5.5, 2.1549458848411773, 6.2, 7.9], 10], [[5.5, 2.1549458848411773, 6.2, 7.9], 9], [[10000000, 9000000, 8000000, 6000000, -200, 10000000], 10000001], [[10, 20, -30, 40, -50], 12], [[10000000, 9000000, 8000001, 8000000, 7000000, 6000000, 2000000], -200], [[10000000, 9000000, 1998, 8000000, 7000000, 6000000, 2000000, 6000000], 100], [[100, 300, 0.1, 0.2], 9000000], [[5.5, 6.2, 7.9, 5.5], 11], [[1000, 500, 250, 125, 6.635714530100879, 62.5, 31.25], 2000001], [[9, 20, 2000, 40, -50], 499], [[10, 20, 21, -30, 40, -50], 7000001], [[-200, 10, 20, -30, 40, 8000000, -50], 8000000], [[2000000, 8000001, 10000000, 9000000, 10, 8000000, 7000000, 2000000, 6000000, 2000000, 2000000], 10000002], [[100, -200, 0, 500, 300], 9], [[100, -200, 300, -400, 500, -600, 500], 19], [[100, 2000000, 10000002, 500, 8000002], 8000000], [[2000000, 10000000, 9000000, 10, 8000000, 7000000, 6000000, 2000000, 7000000], 10000000], [[5.5, 2.8, 8.1], 7000001], [[], 999], [[-200, 300, 8000000, -400, -600, 300, 300], 125], [[5.5, 6.2, 8.462009039856612, 8.565673083320917], 10], [[2000000, 8000001, 1000, 10000000, 8000001, 10, 8000000, 2000000, 6000000, 2000000, 2000000], 9999998], [[5.5, 6.2, 7.9, 8.1, 8.855464118192813, 5.6573184258702085, 6.2], 10], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000], 10000000], [[8000001, 9999998, 10000000, 9000000, 10, 9999999, 8000000, 7000000, 6000000, 2000000, 9999998], 20], [[10000000, 9000000, 8000001, 8000000, 7000000, 6000001, 2000000, 7000000], 125], [[10, 20, 1000, -30, 40, -50], 15], [[10, 20, -30, 0, 40, -50], 13], [[2000000, 10000000, 9000000, 8000000, 6000001, 2000000, 8000000], -50], [[2000000, 10000000, 10, 200, 7000000, 6000000, 2000000], 10000000], [[100, -200, 300, 9999998, -400, 500, 499, -600], 10000002], [[2000000, 10000000, 9000000, -30, 10, 8000000, 6000000, 2000000, 8000000], -2], [[100, -200, -400, 500], 6000000], [[2000000, 8000001, 10000000, 9000000, 10, 8000000, 7000000, 2000000, 6000000, 10, 2000000, 2000000], 10000001], [[100, -200, -400, 500, -600], 40], [[5.5, 6.2, 7.9, 6.287047990560678, 7.938381848412779, 8.1, 7.9], 10000000], [[10, 6000001, -30, 40, -50], 13], [[5.5, 6.2, 7.9, 8.1], 9999999], [[10, 20, -30, 40, -50, 20], 126], [[10000000, 9000000, 8000001, 8000000, 7000000, 6000000, 2000001], 10000001], [[5.5, 6.2, 7.9, 8.1, 8.855464118192813, 5.6573184258702085, 11.869088428731756, 6.2], 10000001], [[100, 9999999, -400, 19], 8000001], [[8000001, 1000, 9999998, 10000000, 9000000, 10, 9999999, 8000000, 7000000, 6000000, 2000000, 9999998], 20], [[], 2000], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 7999999], 125], [[-200, 10, 20, -30, 40, -50], 9000000], [[-200, 10, -200, 11, -30, 40, -50], 8000000], [[5.5, 2.1549458848411773, 6.2, 7.9], 9999999], [[10, 20, -30, 40, 500, 20], 126], [[10000000, 9000000, 8000000, 7000000, 6000000, 2000000, 6000000], 99], [[2.194922883433771, 6.2, 7.9, 8.1], 9999999], [[True, False, True, False, False, False, True, False, True, False], -1], [[1000, 500, 250, 125, 6.635714530100879, 62.5, 31.25, 31.25], 499], [[2000000, 501, 10000000, 9000000, 8000000, 6000000, 2000000, 8000000, 8000000], 10000001], [[10, 20, 14, 40, -50], 12], [[10, 20, -30, 40, -50, -50], 12], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000, 10000001], 8000002], [[5.5, 6.2, 7.9, 8.1, 6.2, 6.2], 1], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 7999999], 200], [[100, -200, 300, -400, 500], 12], [[0.1], 1001], [[100, -200, 300, -400, 500, 499, -600], 9000000], [[1000, 500, 250, 125, 6.635714530100879, 62.5, 31.25, 31.25, 100], 499], [[2000000, 10000001, 9000000, 8000000, 6000000, 2000000, 8000000], 10000001], [[2000000, 10000002, 8000002], 2000], [[5.5, 6.2, 7.934953681964755, 8.1, 5.6573184258702085, 6.2], 10], [[10, 20, -30, 40, -50, -50], -61], [[2000000, 10000000, 9000000, 8000000, 6000000, 8000000], 9999999], [[100, 2000000, 300, -400, 500], -1], [[10, 20, -30, 40, 499, -30], 14], [[5.5, 2.8, 6.2, 8.1], 2000001], [[100, 2000, -200, 0, 500, 300], 13], [[2000000, 9000000, 8000000, 6000000, 2000001, 8000000], -51], [[100, 9999999, -400], 8000001], [[8000001, 9999998, 9000000, 10, 9999999, 8000000, 7000000, 6000000, 2000000], 10000001], [[100, -200, 300, -400, 500, -600, 300], 1], [[2000000, 9000000, 8000000, 6000000, 2000001, 8000000], -52], [[2000000, 10000000, 200, 7000000, -30, 6000000, 2000000], 10000000], [[5.5, 6.2, 7.9, 8.565673083320917], 13], [[6.2, 7.9, 8.1, 6.2, 6.2], 8000001], [[10000000, 9000000, 10000001, 10, 8000000, 6000000, 2000000, 10000001, 10000000], 10], [[2000000, 10000000, 9000000, 8000000, 6000000, 2000000, 7999999, 2000000], 200], [[10000000, 9000000, 10000001, 9, 8000000, 6000000, 10000001], -400], [[10, 20, 21, 300, -30, 40, 11, 10], 10], [[10, 20, -30, -50, 40], 13], [[5.5, 2.1549458848411773, 6.2, 7.9], -30], [[-200, 300, 8000000, -400, -600, 300, -200], 100], [[10000000, 9000000, 10000001, 2000001, 10, 8000000, 6000000, 2000000], 10], [[5.5, 6.2, 7.9], -1], [[9, 20, 40, -50], 499], [[-200, 300, 8000000, -600, 300], 100], [[100, 9999999, -400, 19], 8000000], [[2.194922883433771, 6.2, 7.9, 8.1], 9999998], [[5.5, 2.194922883433771, 6.2, 8.1], 125], [[100, 1999999, 2000000, 300, 500, -600], 8000000], [[10, 20, -30, 40, -50], 16], [[5], 5], [[10], 5], [[4], 5], [[5, 5, 5], 5], [[1, 2, 3, 4], 5], [[10, 20, 30], 5], [[-5, 10, -3, 1], 0], [[0, 0, 0, 0], 5], [[-5, -4, -3], -6], [[10000000, 9000000, 8000000, 7000000, 6000000, 2000000], 2000], [[10, 20, -30, 40, -50], 6000000], [[100, 200, 300, 0.1, 0.2, 0.3], 6000000], [[10, 20, -30, 40, -50, 20], 6000000], [[10000000, 9000000, 8000000, 2000, 6000000, 2000000], 2000], [[5.5, 6.2, 7.9, 8.1], 300], [[6.2, 7.9, 8.1], 300], [[100, 200, 300, 0.1, 0.2, 0.3], 40], [[5.5, 6.2, 7.9], -200], [[5.5, 6.2, 7.9], 8000000], [[5.5, 6.2, 7.9], 300], [[100, 200, 300, 0.1, 0.2, 0.3, 0.2], 0], [[5.5, 6.2, 7.9, 7.9], 300], [[6.2, 7.9, 7.9], 300], [[10000000, 9000000, 8000000, 2000, 6000000, 2000000], 10000001], [[100, 200, 300, 0.1, 0.2, 0.3, 0.2, 100], 0], [[100, -200, 300, -400, 500, -600], 2000], [[6.2, 7.9], -201], [[1000, 500, 250, 125, 62.5, 30.807804019985152], 2000], [[1000, 0.7, 500, 250, 125, 62.5, 31.25], 2000], [[6.4133956835438735, 7.9], -200], [[10, 20, 15, 40, -50, 20], 6000000], [[7.9, 7.9, 7.9], 1000], [[10, 20, -30, 40, -50, 20], 9], [[100, 200, 300, 0.06967522411157957, 0.2, 0.3, 0.2, 100], 0], [[1000, 500, 250, 125, 62.5, 30.807804019985152], 8000000], [[10, 20, -30, -51, 40, -50, 20], 6000000], [[5.766499924540022, 7.9, 7.9], 300], [[5.5, 6.2, 7.9, 6.2], 300], [[10, 20, -51, 40, -50, 20], 6000000], [[5.5, 6.2, 7.9, 6.2], 301], [[100, 200, 300, 0.1, 0.2, 0.3, 0.2], 40], [[10000000, 9000000, 8000000, 2000, 6000000, 500, 2000000], 2000], [[10, 20, -51, 40, -50, 200, 20], 6000000], [[5.5, 6.2212876393256, 6.2, 7.9, 6.2], 302], [[1000, 500, 250, 125, 62.5, 30.807804019985152, 500], 2001], [[1000, 500, 250, 62.5, 30.807804019985152], 2000], [[5.5, 5.50048632089892, 7.9, 7.9], 300], [[1000, 500, 250, 62.5, 30.807804019985152, 62.5], 2000], [[5.5, 6.2, 8.8519061638015], 300], [[5.5, 5.50048632089892, 7.9], 300], [[5.5, 7.9], -200], [[10000000, 9000000, 8000000, 2000, 6000000, 100, 8000000], 2000], [[5.5, 7.9], -199], [[100, 200, 300, 0.1, 0.2, 0.3, 0.2, 100], 9], [[1000, 500, 250, 62.5, 30.807804019985152], -200], [[500, 250, 62.5, 30.807804019985152], 2000], [[6.576799211228067, 5.5, 5.50048632089892, 6.2212876393256, 7.9, 7.9], 300], [[100, 200, 300, 0.1, 0.2, 0.3], 302], [[6.2, 7.9], 250], [[6.576799211228067, 5.5, 5.50048632089892, 6.2212876393256, 7.9], 300], [[10, 20, -30, 39, 40, -50], 6000000], [[5.5, 7.9], 2001], [[5.871122108907659, 6.2, 7.9, 6.2], 301], [[5.5, 6.2212876393256, 6.2, 7.9, 6.2], -200], [[10, 20, -30, 39, 40, -50], 302], [[1000, 500, 250, 6000000, 62.5, 31.25], 2000], [[10000000, 9000000, 8000000, 2000, 6000000, 2000000], 10000000], [[5.5, 5.50048632089892, 0.5, 7.9, 7.9], 300], [[6.2, 7.9], 299], [[1000, 500, 250, 125, 30.807804019985152, 500], 2001], [[10, 20, -30, -51, 40, -50, 20], -399], [[10000000, 9000000, 8000000, 2000, 6000000, 500, 2000000], 15], [[5.5, 6.6284378542197375, 5.50048632089892, 7.9, 7.9], 300], [[6.990844960737688, 5.5, 6.2, 7.9, 8.1], 300], [[6.2], -201], [[100, 200, 0.1, 0.2, 0.3, 0.2], 0], [[5.5, 6.38359489632532, 8.8519061638015], 300], [[6.2, 7.9, 7.9], 299], [[1.430414675639685, 6.2, 7.9, 0.32055210364227493], 300], [[100, 200, 300, 0.2, 0.3], 1], [[7.9, 7.9, 7.9, 7.9], 1000], [[5.5, 6.878384299672373, 7.9], 15], [[30, 97, 90, -200, 59], 0], [[30, 97, 90, 59], 0], [[5.5, 6.6284378542197375, 5.50048632089892, 7.9, 7.9], 299], [[1000, 500, 250, 125, 62.5, 30.807804019985152], 7999999], [[6.2, 7.9, 6.2], -201], [[1000, 500, 250, 62.5, 62.534685136963134, 30.807804019985152, 62.5], 2000], [[10000000, 9000000, 8000000, 2000, 6000000, 100, 8000000], -50], [[6.110733640513043, 5.5, 6.2], 8000000], [[10, 20, -51, 40, -50, 20, 40], 6000000], [[10, 20, -51, 40, -50, 20, -51], 6000001], [[100, 200, 300, 0.1, 0.2, 0.3, 0.2, 100], 8], [[2.5, 7.9, 7.9, 7.9], 1000], [[1000, 500, 250, 62.5, 30.807804019985152, 62.5], 200], [[-400, 100, -200, 300, -400, 500, -600, -600], 302], [[100, 200, 300, 0.06967522411157957, 0.2, 0.3, 0.2, 100, 0.2], 0], [[10000000, 9000000, 8000000, 2000, 6000000, 100, 8000000], 10000001], [[5.871122108907659, 6.2, 7.9], 301], [[7.9, 7.9, 7.9, 7.9, 7.9], 1000], [[6.576799211228067, 5.5, 1.5311576847949309, 5.50048632089892, 6.2212876393256, 7.9, 7.9], -199], [[3.284373826304595, 1000, 500, 250, 62.5, 30.807804019985152, 500], 2000], [[7.9, 7.9, 7.9, 7.9, -0.28791951724548404, -0.28791951724548404], 1000], [[0.2, 62.5, -63.579573934400166, 0.5, 98.82739614126038, -0.28791951724548404, -50.78504214587984, 58.062454697705476, 55.110190228263775, 10.520189946545017], 0], [[10, 20, -30, 40, -50], 59], [[1000, 500, 250, 62.5, 30.807804019985152, -50.78504214587984, 62.5], 2000], [[10000001, -200, 300, -400, 500, -600], 1999], [[5.5, 6.2], 300], [[10000000, 9000000, 7999999, 2000, 6000000, 2000000], 10000001]]
    results = [True, False, True, True, True, False, True, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, True, False, True, False, True, True, True, True, False, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, True, True, False, True, False, False, False, False, True, False, True, False, False, True, False, False, False, False, True, False, True, True, True, False, True, False, False, True, False, True, True, True, False, False, True, True, False, False, True, True, False, True, True, True, True, True, True, False, False, False, True, False, True, False, True, True, True, True, True, True, True, False, True, False, True, False, True, True, True, True, False, True, True, True, True, False, True, False, True, True, False, False, True, True, False, True, True, False, True, True, True, False, False, True, True, False, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True, False, True, False, False, False, True, False, True, True, False, True, False, False, False, True, False, True, False, True, True, False, False, False, True, True, False, False, True, False, False, True, False, True, False, False, True, True, False, True, False, True, True, True, False, False, True, True, True, True, False, False, False, True, True, True, False, True, False, True, False, False, False, False, True, True, False, True, False, True, False, False, False, False, False, False, False, True, False, True, True, False, True, False, True, True, True, True, False, False, True, False, True, True, True, False, False, True, False, False, True, False, False, False, False, False, False, True, True, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, True, True, True, False, False, False, True, False, True, False, False, True, False, False, True, True, True, False, True, True, False, False, True, True, False, True, True, True, False, True, False, True, True, False, True, True, False, False, True, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, False, True, False, False, True, True, True, False, False, True, True, False, False, True, True, True, False, True, True, False, False, True, True, False, True, False, True, True, True, False, True, False, False, False, True, True, True, False, True, True, False, True, True, False, True, True]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(below_threshold)