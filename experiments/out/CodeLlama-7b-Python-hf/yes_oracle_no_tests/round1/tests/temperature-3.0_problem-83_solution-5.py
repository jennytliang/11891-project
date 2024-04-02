def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Initialize the count
    count = 0
    
    # If n is 1 then we have 10 numbers that start or end with 1
    if n == 1:
        return 10
    
    # If n is 2 then we have 9 numbers that start or end with 1
    elif n == 2:
        return 9
    
    # If n is 3 then we have 9 numbers that start or end with 1
    elif n == 3:
        return 9
    
    # If n is 4 then we have 8 numbers that start or end with 1
    elif n == 4:
        return 8
    
    # If n is 5 then we have 8 numbers that start or end with 1
    elif n == 5:
        return 8
    
    # If n is 6 then we have 7 numbers that start or end with 1
    elif n == 6:
        return 7
    
    # If n is 7 then we have 7 numbers that start or end with 1
    elif n == 7:
        return 7
    
    # If n is 8 then we have 6 numbers that start or end with 1
    elif n == 8:
        return 6
    
    # If n is 9 then we have 6 numbers that start or end with 1
    elif n == 9:
        return 6
    
    # If n is 10 then we have 5 numbers that start or end with 1
    elif n == 10:
        return 5
    
    # If n is 11 then we have 5 numbers that start or end with 1
    elif n == 11:
        return 5
    
    # If n is 12 then we have 4 numbers that start or end with 1
    elif n == 12:
        return 4
    
    # If n is 13 then we have 4 numbers that start or end with 1
    elif n == 13:
        return 4
    
    # If n is 14

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