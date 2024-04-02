def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # return the count of the numbers of n-digit
    # positive integers that start or end with 1.
    return 0


# Pytest
import pytest

# Tests
@pytest.mark.parametrize("n, expected_result", [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 10),
    (7, 15),
    (8, 21),
    (9, 28),
    (10, 36),
    (11, 45),
    (12, 55),
    (13, 66),
    (14, 78),
    (15, 91),
    (16, 105),
    (17, 120),
    (18, 136),
    (19, 153),
    (20, 171),
])
def test_starts_one_ends(n, expected_result):
    assert starts_one_ends(n) == expected_result


# Run with Python
if __name__ == "__main__":
    print(starts_one_ends(10))


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


    if n == 1: return 1
    return 18 * 10 ** (n - 2)



def check(candidate):
    inputs = [[1], [2], [3], [4], [5], [6], [10], [12], [15], [20], [30], [8], [25], [100], [500], [29], [14], [26], [19], [13], [9], [101], [28], [21], [24], [7], [102], [99], [16], [501], [17], [22], [98], [11], [499], [1000], [1234], [9876], [31415], [1000000], [99999], [9877], [9878], [1235], [1001], [9879], [9880], [999999], [9881], [31414], [78], [999998], [999], [1002], [100000], [9882], [1233], [80], [999997], [1236], [1237], [1232], [79], [90], [31416], [31413], [31412], [31411], [1003], [999996], [68], [69], [1004], [97], [23], [9883], [89], [31417], [1231], [67], [100001], [50], [94], [82], [53], [52], [51], [9874], [31418], [77], [54], [9875], [76], [9873], [1000001], [96], [49], [1000002], [75], [998], [35], [39], [48], [34], [70], [38], [95], [997], [47]]
    for i, inp in enumerate(inputs):
        assertion(candidate(*inp), ref_func(*inp), 0)


check(starts_one_ends)