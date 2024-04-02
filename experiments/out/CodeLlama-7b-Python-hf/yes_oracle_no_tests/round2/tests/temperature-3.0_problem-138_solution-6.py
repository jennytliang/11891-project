def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: pass def is _ equal
	"""
    # YOUR CODE HERE
    if n % 2 == 1:
        return False
    else:
        even_num = n / 2
        even_num_list = list(range(even_num, 0, -2))
        for i in even_num_list:
            for j in even_num_list:
                for k in even_num_list:
                    for l in even_num_list:
                        if i + j + k + l == n:
                            return True
        return False



def sum_of_divisors(n):
    """Return the sum of all positive integer divisors of n
    Example
    sum_of_divisors(6) == 12
    sum_of_divisors(12) == 31
    
	Do not include these tokens in the code: pass def sum_of_divisors
	"""
    # YOUR CODE HERE
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)



def is_prime(n):
    """Evaluate whether the given number n is prime
    Example
    is_prime(2) == True
    is_prime(8) == False
    
	Do not include these tokens in the code: pass def is_prime
	"""
    # YOUR CODE HERE
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True



def is_prime_with_divisors(n):
    """Evaluate whether the given number n is prime and has exactly 4 positive integer divisors
    Example
    is_prime_with_divisors(7) == True
    is_prime_with_divisors(12) == False
    
	Do not include these tokens in the code: pass def is_prime_with_divisors
	""



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