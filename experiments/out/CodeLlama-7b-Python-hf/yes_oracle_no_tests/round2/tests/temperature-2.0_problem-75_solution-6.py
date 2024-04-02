def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # write code here
	"""
    # 1. Check if a is a multiple of 2
    # 2. If it is not, check if it is a multiple of 3
    # 3. If it is not, check if it is a multiple of 5
    # 4. If it is not, then it is not a multiple of 2, 3, or 5
    # 5. If it is a multiple of 2, 3, or 5, check if it is the product of 2 prime numbers
    # 6. If it is the product of 2 prime numbers, return True
    # 7. If it is not, return False
    
    # 1. Check if a is a multiple of 2
    if a % 2 == 0:
        # 2. If it is not, check if it is a multiple of 3
        if a % 3 != 0:
            # 3. If it is not, check if it is a multiple of 5
            if a % 5 != 0:
                # 4. If it is not, then it is not a multiple of 2, 3, or 5
                return False
            # 5. If it is a multiple of 5, check if it is the product of 2 prime numbers
            elif a % 5 == 0:
                # 6. If it is the product of 2 prime numbers, return True
                if (a / 5) % 2 == 0 and (a / 5) % 3 != 0:
                    return True
        # 7. If it is a multiple of 3, check if it is the product of 2 prime numbers
        elif a % 3 == 0:
            # 6. If it is the product of 2 prime numbers, return True
            if (a / 3) % 2 != 0 and (a / 3) % 5 != 0:
                return True
    # 8. If it is a multiple of 2, check if it is the product of 2 prime numbers
    elif a % 2 == 0:
        # 6. If it is the product of 2 prime numbers,



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
    inputs = [[5], [30], [8], [10], [33], [49], [77], [91], [99], [6], [90], [98], [25], [21], [48], [20], [22], [32], [26], [78], [19], [47], [31], [29], [-98], [-37], [-38], [28], [18], [23], [-92], [-2], [57], [-99], [58], [56], [-1], [92], [1], [-80], [34], [-75], [-100], [-95], [16], [-94], [17], [59], [-7], [93], [-82], [-15], [-81], [-96], [-74], [2], [3], [7], [97], [42], [-101], [43], [44], [45], [-56], [60], [-55], [46], [62], [55], [61], [41], [40], [-57], [63], [-102], [52], [-72], [-97], [94], [12], [89], [53], [0], [64], [-58], [65], [-71], [95], [35], [-70], [96], [-59], [15], [-33]]
    results = [False, True, True, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(is_multiply_prime)