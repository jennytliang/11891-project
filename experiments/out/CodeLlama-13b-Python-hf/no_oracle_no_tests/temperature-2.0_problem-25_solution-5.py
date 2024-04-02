from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n == 1:
        return [1]
    i = 2
    result = []
    while i ** 2 <= n:
        while n % i == 0:
            n //= i
            result.append(i)
        i += 1
    if n > 1:
        result.append(n)
    return result




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
    inputs = [[2], [4], [8], [57], [3249], [185193], [20577], [18], [10], [15], [28], [1024], [131], [33], [1000], [100], [123456789], [987654321], [1025], [11], [1026], [29], [1027], [14], [34], [13], [99], [132], [123456790], [1023], [123456788], [32], [31], [1022], [987654320], [123456791], [1028], [123456787], [123456792], [27], [39], [12], [30], [2147483647], [1207943], [112234369], [999983], [1003001001], [43121192843], [1073741789], [9999999967], [1003001000], [112234370], [56], [9999999966], [2147483646], [1003000999], [1207942], [999984], [79], [80], [1003001002], [78], [77], [112234368], [9999999965], [83], [76], [75], [112234367], [52], [112234371], [2147483645], [53], [9999999964], [112234372], [1003001004], [101], [6], [1003001005], [1073741788], [67], [123456786], [1003001003], [47], [58], [26], [51], [55], [38], [37], [17], [125], [7919], [987654322], [43121192841], [43121192844], [987654323], [43121192842], [123456785], [112234366], [999982], [112234365], [43121192845], [2147483644], [1207944], [1073741790], [1073741791], [9999999969], [2147483643], [1207945], [43121192840], [1207946], [1003000998], [43121192839], [112234364], [9999999968], [987654324], [1207947], [999980], [999979], [999981], [43121192838], [987654319], [999985], [2147483642], [2147483641], [46], [43121192837], [999987], [987654325], [1003000997], [987654326], [1207948], [999986], [987654327], [50], [999978], [999988], [999977], [999989], [9999999963], [44], [43], [42]]
    results = [[2], [2, 2], [2, 2, 2], [3, 19], [3, 3, 19, 19], [3, 3, 3, 19, 19, 19], [3, 19, 19, 19], [2, 3, 3], [2, 5], [3, 5], [2, 2, 7], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [131], [3, 11], [2, 2, 2, 5, 5, 5], [2, 2, 5, 5], [3, 3, 3607, 3803], [3, 3, 17, 17, 379721], [5, 5, 41], [11], [2, 3, 3, 3, 19], [29], [13, 79], [2, 7], [2, 17], [13], [3, 3, 11], [2, 2, 3, 11], [2, 5, 37, 333667], [3, 11, 31], [2, 2, 7, 13, 17, 71, 281], [2, 2, 2, 2, 2], [31], [2, 7, 73], [2, 2, 2, 2, 5, 37, 333667], [123456791], [2, 2, 257], [31, 31, 128467], [2, 2, 2, 3, 59, 87187], [3, 3, 3], [3, 13], [2, 2, 3], [2, 3, 5], [2147483647], [11, 11, 67, 149], [13, 8633413], [999983], [3, 31, 10784957], [26731, 1613153], [1073741789], [9999999967], [2, 2, 2, 5, 5, 5, 1003001], [2, 5, 11223437], [2, 2, 2, 7], [2, 3, 11, 457, 331543], [2, 3, 3, 7, 11, 31, 151, 331], [7, 11, 13, 41, 24439], [2, 41, 14731], [2, 2, 2, 2, 3, 83, 251], [79], [2, 2, 2, 2, 5], [2, 181, 631, 4391], [2, 3, 13], [7, 11], [2, 2, 2, 2, 2, 2, 2, 3, 19, 15383], [5, 29, 1327, 51971], [83], [2, 2, 19], [3, 5, 5], [7, 16033481], [2, 2, 13], [3, 37411457], [5, 19, 22605091], [53], [2, 2, 17, 17, 31, 173, 1613], [2, 2, 28058593], [2, 2, 3, 3, 27861139], [101], [2, 3], [5, 200600201], [2, 2, 7, 2341, 16381], [67], [2, 3, 20576131], [17, 59, 101, 9901], [47], [2, 29], [2, 13], [3, 17], [5, 11], [2, 19], [37], [17], [5, 5, 5], [7919], [2, 701, 704461], [3, 3, 131, 1237, 29567], [2, 2, 3, 3593432737], [987654323], [2, 7, 13, 5717, 41443], [5, 24691357], [2, 56117183], [2, 79, 6329], [3, 3, 5, 23, 108439], [5, 8624238569], [2, 2, 233, 1103, 2089], [2, 2, 2, 3, 3, 19, 883], [2, 3, 5, 11, 47, 107, 647], [29, 97, 381707], [3, 3333333323], [3, 715827881], [5, 241589], [2, 2, 2, 5, 11, 98002711], [2, 31, 19483], [2, 3, 167, 1000999], [239, 180423401], [2, 2, 11, 643, 3967], [2, 2, 2, 2, 2, 7, 7, 6377551], [2, 2, 3, 443, 185789], [3, 13, 47, 659], [2, 2, 5, 49999], [999979], [3, 3, 111109], [2, 3, 7186865473], [987654319], [5, 7, 28571], [2, 23, 46684427], [2699, 795659], [2, 23], [769, 2383, 23531], [3, 257, 1297], [5, 5, 7, 337, 16747], [23, 317, 137567], [2, 131, 3769673], [2, 2, 7, 7, 6163], [2, 13, 38461], [3, 11, 31, 163, 5923], [2, 5, 5], [2, 3, 7, 29, 821], [2, 2, 11, 22727], [11, 90907], [19, 52631], [3, 3, 3, 370370369], [2, 2, 11], [43], [2, 3, 7]]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(factorize)