def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i).count("7") > 0:
                count += 1
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()




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
    inputs = [[50], [78], [79], [100], [200], [4000], [10000], [100000], [1], [10], [20], [30], [70], [71], [72], [73], [74], [75], [31], [69], [9], [77], [76], [8], [2], [21], [68], [22], [29], [23], [32], [3], [11], [33], [19], [86], [7], [12], [4], [28], [6], [60], [85], [5], [80], [61], [59], [62], [63], [84], [18], [27], [81], [64], [26], [83], [82], [13], [66], [24], [34], [43], [42], [14], [65], [67], [94], [25], [51], [17], [52], [41], [40], [16], [58], [15], [555555], [303], [12345], [2000], [9999], [123456], [304], [9998], [12344], [302], [12346], [12347], [12348], [12343], [123455], [123454], [555554], [123453], [10001], [301], [123457], [12341], [1999], [12342], [123452], [555556], [9997], [92], [90], [91], [123451], [93], [12350], [555552], [12351], [555551], [123458], [9996], [12352], [555550], [555557], [12340], [10002], [555553], [555558], [44], [12349], [555549], [45], [123459], [12339], [305], [49], [300], [555559], [555560], [123460], [95], [1000], [2001], [2002], [2004], [1998], [2003], [53], [54], [2005], [555561], [1997], [55], [48], [555562], [1996], [47], [306], [307]]
    results = [0, 2, 3, 3, 6, 192, 639, 8026, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43688, 10, 747, 95, 639, 9487, 10, 639, 747, 10, 747, 747, 747, 747, 9487, 9487, 43688, 9487, 639, 10, 9487, 747, 95, 747, 9487, 43688, 638, 3, 3, 3, 9487, 3, 747, 43688, 747, 43688, 9487, 638, 747, 43688, 43688, 747, 639, 43688, 43688, 0, 747, 43688, 0, 9487, 747, 10, 0, 10, 43688, 43688, 9487, 3, 47, 95, 95, 95, 95, 95, 0, 0, 95, 43688, 95, 0, 0, 43688, 95, 0, 10, 10]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(fizz_buzz)