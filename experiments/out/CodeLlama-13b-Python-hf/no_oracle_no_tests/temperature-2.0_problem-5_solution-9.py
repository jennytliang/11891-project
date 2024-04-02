from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers.insert(0, delimeter)
    numbers.insert(0, delimeter)

    for i in range(3, len(numbers), 2):
        numbers.insert(i, delimeter)

    return numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)




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
    inputs = [[[], 7], [[5, 6, 3, 2], 8], [[2, 2, 2], 2], [[1, 2, 3], 0], [[2, 4, 6, 8], 1], [[9, 9, 9, 9, 9, 9], 7], [[10], 5], [[5, 7], 2], [[1, 3, 5, 7], 4], [[2, 3], 1], [[5, 10, 15], 0], [[0, 0, 0], 7], [[1, 9, 5, 6], 3], [[2, 3], 0], [[0, 0, 0], 8], [[1, 2, 3, 2], 0], [[7], 2], [[3], 1], [[5, 7], 3], [[5, 7], 5], [[], 2], [[9, 9, 9, 9, 9, 9, 9], 7], [[5, 7], 15], [[3], 0], [[1, 9, 5, 6, 5], 3], [[2, 2], 1], [[0, 0, 0, -1], 7], [[7, 9], 15], [[2, 3, 2, -46], 0], [[], 1], [[3], 7], [[1, 1, 1, 1, 1, 1], 0], [[-2, 5, 10, -5, 2], -8], [[3, 6, 2, 5, 1, 9], 0], [[7, 3, 6, 8, 4, 2, 1], -1], [[4, 1, 2, 3], 4], [[1, 2, 3, 4], 4], [[4], 4], [[-1, -2, -3], -4], [[1, 2, 3, 4], 10000], [[], 8], [[3, 4], 10000], [[3, 4], -8], [[3, 6, 2, 5, 1, 9], 1], [[-2, 5, 10, -5, 2], -7], [[3, 6, 2, 3, 5, 1], -1], [[1, 1, 1, 1, 1, 1], -5], [[4], -5], [[1, 3, 4], 10000], [[2, 3, 4], 10000], [[-2, 3, 4], -8], [[-2, 5, 10, -5, 2, 5], 5], [[4, 4], -5], [[1, 3, 4, 1], 6], [[1, 2, 3, 4], 6], [[3, 6, 5, 1, 9], 0], [[-2, 2, 5, 10, -5, 2], -7], [[7, 1, 1, 1, 1, 1, 1], -5], [[3, 7, 5, 1, 9], 9], [[1, 2, 3, 4], 9], [[3, 2, 4], -8], [[2, 3, 4], 5], [[7, 1, 1, 1, 1, 1], -5], [[3, 7, 5, 6, 1, 9], 9], [[2, 3, 4], 10001], [[-2, 2, 4, 4], -8], [[4, 4], -4], [[7, 1, 1, 1, 1, 1, 1], -3], [[3, 3, 4], 5], [[3, 7, 2, 1, 9], 1], [[6, 3, 7, 5, 1, 9, 3], 7], [[1, 2, 3, 4], 9999], [[3, 7, 5, 7, 9], 9], [[6, 3, 7, 7, 1, 9, 3], 7], [[], -5], [[1, 1, 1, 1, 1, 1, 1], 10000], [[3, -4, 6, 5, 1, 9], 1], [[7, 3, 6, 8, 4, 2, 1], 10], [[-2, 7, 2, 1, 9], 2], [[5, 15, 63, 2, -2, 5, 9, 100, 5, -9], 8], [[1, 2, 4, 4], 6], [[3, 4], -5], [[3, 6, 5, 1, 9, 6, 1], 0], [[7, 1, 1, 1, 1, 1, 7], -5], [[1, 1, 1, 1, 1, 1], -6], [[7, 1, 1, 1, 1, 1, 1], -4], [[-2, 7, 2, 1, -1], 2], [[3, 6, 5, 1, 9, 6, 1], 10001], [[-4, -4, 6, 5, 1, 9], 1], [[-6, 4], 4], [[-4, -4, 6, 5, 1, 9], 2], [[3, 63, 3], 10000], [[3, 63, 3, 3], 10000], [[4], 63], [[3, 6, 5, 1, 9, 1], 0], [[4, 1, 2, 3, 2], 2], [[-2, 2, 4, 4], -7], [[7, 3, 6, 8, 4, 2, 2], 10], [[5, 15, 63, 2, -2, 5, 9, 100, 5, -9, 100], 8], [[15, 63, 2, -2, 5, -93, 100, 5, -9], 9], [[7, 1, 1, 1, 1, 2], -4], [[4, 4, 4], -5], [[], 4], [[4], 8], [[9, 3], 6], [[5, 5], 5], [[1, 1, 2, 2, 3, 3], 4], [[2, 3, 3, 2], 3], [[], 0], [[5], 2], [[2, 3, 4], 1], [[5, 6, 7, 8], 5], [[1, 2, 4, 4], 3], [[1, 2, 3, 4, 1], 0], [[1, 2, 4, 4], 2], [[7, 3, 6, 8, 4, 2, 1, 3], -1], [[4, 1, 1, 2, 3], 4], [[3, 6, 2, 5, 1], 0], [[-1, 1, -2, -3], -3], [[1, 2, 3], 4], [[4, 1, 2, 3, 3], 7], [[10, -2, 5, 10, -5, 2, 10], -8], [[1, 1, 1, 1, 1], 0], [[4, 4], 4], [[4, 1, 2, 3], 6], [[1, 1, 4, 4], -2], [[4, 1, 2, 3, 3, 4], 3], [[-1, -2, -3], 2], [[4, 1, 2, 3, 3, 4], 10000], [[3, 1, 2, 3, 4], 10000], [[3, 4, 4, 4], 3], [[-1, -2, -3, -3], 2], [[3, 2, 3, 4], 10000], [[-48, 4, 1, 2, 3], 3], [[3, -8, 3, 4], -48], [[4, 1, 2, 3, 3, -5], 10000], [[-22, 1, 2, 18], 5], [[7, 3, 6, 8, 4, 2, 1, 3, 4], -1], [[1, 2, 4], -1], [[4], 9], [[1, 2, 4, 4, 1], 2], [[1, 2, 4], 0], [[4, 4, 4], 4], [[1, 2], 0], [[1, 1, 2, 3], 0], [[3, -8, 4, 4], -48], [[2, 3, 4], 4], [[3, 2, 3, 4, 3], 19], [[10, -2, 5, 10, -5, 2, 10], -9], [[-1, 1, -2, -2, -3], 10000], [[-22, 1, 2, 18, 1], 5], [[3, -8, 3, 4, -8], -48], [[-22, 1, 2, -52], 5], [[1, 2, 4, 4], 0], [[1, 2, -9, 4, 4], 0], [[1, 1, 1, 2, 1], 0]]
    results = [[], [5, 8, 6, 8, 3, 8, 2], [2, 2, 2, 2, 2], [1, 0, 2, 0, 3], [2, 1, 4, 1, 6, 1, 8], [9, 7, 9, 7, 9, 7, 9, 7, 9, 7, 9], [10], [5, 2, 7], [1, 4, 3, 4, 5, 4, 7], [2, 1, 3], [5, 0, 10, 0, 15], [0, 7, 0, 7, 0], [1, 3, 9, 3, 5, 3, 6], [2, 0, 3], [0, 8, 0, 8, 0], [1, 0, 2, 0, 3, 0, 2], [7], [3], [5, 3, 7], [5, 5, 7], [], [9, 7, 9, 7, 9, 7, 9, 7, 9, 7, 9, 7, 9], [5, 15, 7], [3], [1, 3, 9, 3, 5, 3, 6, 3, 5], [2, 1, 2], [0, 7, 0, 7, 0, 7, -1], [7, 15, 9], [2, 0, 3, 0, 2, 0, -46], [], [3], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [-2, -8, 5, -8, 10, -8, -5, -8, 2], [3, 0, 6, 0, 2, 0, 5, 0, 1, 0, 9], [7, -1, 3, -1, 6, -1, 8, -1, 4, -1, 2, -1, 1], [4, 4, 1, 4, 2, 4, 3], [1, 4, 2, 4, 3, 4, 4], [4], [-1, -4, -2, -4, -3], [1, 10000, 2, 10000, 3, 10000, 4], [], [3, 10000, 4], [3, -8, 4], [3, 1, 6, 1, 2, 1, 5, 1, 1, 1, 9], [-2, -7, 5, -7, 10, -7, -5, -7, 2], [3, -1, 6, -1, 2, -1, 3, -1, 5, -1, 1], [1, -5, 1, -5, 1, -5, 1, -5, 1, -5, 1], [4], [1, 10000, 3, 10000, 4], [2, 10000, 3, 10000, 4], [-2, -8, 3, -8, 4], [-2, 5, 5, 5, 10, 5, -5, 5, 2, 5, 5], [4, -5, 4], [1, 6, 3, 6, 4, 6, 1], [1, 6, 2, 6, 3, 6, 4], [3, 0, 6, 0, 5, 0, 1, 0, 9], [-2, -7, 2, -7, 5, -7, 10, -7, -5, -7, 2], [7, -5, 1, -5, 1, -5, 1, -5, 1, -5, 1, -5, 1], [3, 9, 7, 9, 5, 9, 1, 9, 9], [1, 9, 2, 9, 3, 9, 4], [3, -8, 2, -8, 4], [2, 5, 3, 5, 4], [7, -5, 1, -5, 1, -5, 1, -5, 1, -5, 1], [3, 9, 7, 9, 5, 9, 6, 9, 1, 9, 9], [2, 10001, 3, 10001, 4], [-2, -8, 2, -8, 4, -8, 4], [4, -4, 4], [7, -3, 1, -3, 1, -3, 1, -3, 1, -3, 1, -3, 1], [3, 5, 3, 5, 4], [3, 1, 7, 1, 2, 1, 1, 1, 9], [6, 7, 3, 7, 7, 7, 5, 7, 1, 7, 9, 7, 3], [1, 9999, 2, 9999, 3, 9999, 4], [3, 9, 7, 9, 5, 9, 7, 9, 9], [6, 7, 3, 7, 7, 7, 7, 7, 1, 7, 9, 7, 3], [], [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000, 1], [3, 1, -4, 1, 6, 1, 5, 1, 1, 1, 9], [7, 10, 3, 10, 6, 10, 8, 10, 4, 10, 2, 10, 1], [-2, 2, 7, 2, 2, 2, 1, 2, 9], [5, 8, 15, 8, 63, 8, 2, 8, -2, 8, 5, 8, 9, 8, 100, 8, 5, 8, -9], [1, 6, 2, 6, 4, 6, 4], [3, -5, 4], [3, 0, 6, 0, 5, 0, 1, 0, 9, 0, 6, 0, 1], [7, -5, 1, -5, 1, -5, 1, -5, 1, -5, 1, -5, 7], [1, -6, 1, -6, 1, -6, 1, -6, 1, -6, 1], [7, -4, 1, -4, 1, -4, 1, -4, 1, -4, 1, -4, 1], [-2, 2, 7, 2, 2, 2, 1, 2, -1], [3, 10001, 6, 10001, 5, 10001, 1, 10001, 9, 10001, 6, 10001, 1], [-4, 1, -4, 1, 6, 1, 5, 1, 1, 1, 9], [-6, 4, 4], [-4, 2, -4, 2, 6, 2, 5, 2, 1, 2, 9], [3, 10000, 63, 10000, 3], [3, 10000, 63, 10000, 3, 10000, 3], [4], [3, 0, 6, 0, 5, 0, 1, 0, 9, 0, 1], [4, 2, 1, 2, 2, 2, 3, 2, 2], [-2, -7, 2, -7, 4, -7, 4], [7, 10, 3, 10, 6, 10, 8, 10, 4, 10, 2, 10, 2], [5, 8, 15, 8, 63, 8, 2, 8, -2, 8, 5, 8, 9, 8, 100, 8, 5, 8, -9, 8, 100], [15, 9, 63, 9, 2, 9, -2, 9, 5, 9, -93, 9, 100, 9, 5, 9, -9], [7, -4, 1, -4, 1, -4, 1, -4, 1, -4, 2], [4, -5, 4, -5, 4], [], [4], [9, 6, 3], [5, 5, 5], [1, 4, 1, 4, 2, 4, 2, 4, 3, 4, 3], [2, 3, 3, 3, 3, 3, 2], [], [5], [2, 1, 3, 1, 4], [5, 5, 6, 5, 7, 5, 8], [1, 3, 2, 3, 4, 3, 4], [1, 0, 2, 0, 3, 0, 4, 0, 1], [1, 2, 2, 2, 4, 2, 4], [7, -1, 3, -1, 6, -1, 8, -1, 4, -1, 2, -1, 1, -1, 3], [4, 4, 1, 4, 1, 4, 2, 4, 3], [3, 0, 6, 0, 2, 0, 5, 0, 1], [-1, -3, 1, -3, -2, -3, -3], [1, 4, 2, 4, 3], [4, 7, 1, 7, 2, 7, 3, 7, 3], [10, -8, -2, -8, 5, -8, 10, -8, -5, -8, 2, -8, 10], [1, 0, 1, 0, 1, 0, 1, 0, 1], [4, 4, 4], [4, 6, 1, 6, 2, 6, 3], [1, -2, 1, -2, 4, -2, 4], [4, 3, 1, 3, 2, 3, 3, 3, 3, 3, 4], [-1, 2, -2, 2, -3], [4, 10000, 1, 10000, 2, 10000, 3, 10000, 3, 10000, 4], [3, 10000, 1, 10000, 2, 10000, 3, 10000, 4], [3, 3, 4, 3, 4, 3, 4], [-1, 2, -2, 2, -3, 2, -3], [3, 10000, 2, 10000, 3, 10000, 4], [-48, 3, 4, 3, 1, 3, 2, 3, 3], [3, -48, -8, -48, 3, -48, 4], [4, 10000, 1, 10000, 2, 10000, 3, 10000, 3, 10000, -5], [-22, 5, 1, 5, 2, 5, 18], [7, -1, 3, -1, 6, -1, 8, -1, 4, -1, 2, -1, 1, -1, 3, -1, 4], [1, -1, 2, -1, 4], [4], [1, 2, 2, 2, 4, 2, 4, 2, 1], [1, 0, 2, 0, 4], [4, 4, 4, 4, 4], [1, 0, 2], [1, 0, 1, 0, 2, 0, 3], [3, -48, -8, -48, 4, -48, 4], [2, 4, 3, 4, 4], [3, 19, 2, 19, 3, 19, 4, 19, 3], [10, -9, -2, -9, 5, -9, 10, -9, -5, -9, 2, -9, 10], [-1, 10000, 1, 10000, -2, 10000, -2, 10000, -3], [-22, 5, 1, 5, 2, 5, 18, 5, 1], [3, -48, -8, -48, 3, -48, 4, -48, -8], [-22, 5, 1, 5, 2, 5, -52], [1, 0, 2, 0, 4, 0, 4], [1, 0, 2, 0, -9, 0, 4, 0, 4], [1, 0, 1, 0, 1, 0, 2, 0, 1]]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(intersperse)