def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    
	Include these tokens in the code: import random def mill er _ ra bin
	Do not include these tokens in the code: if n == 1 :
	"""
    fib_list = [2, 3]
    while len(fib_list) <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    for i in range(2, fib_list[-1]):
        if i % 2 == 0:
            continue
        if i % 5 == 0:
            continue
        if i % 3 == 0:
            continue
        if i % 7 == 0:
            continue
        if i % 11 == 0:
            continue
        if i % 13 == 0:
            continue
        if i % 17 == 0:
            continue
        if i % 19 == 0:
            continue
        if i % 23 == 0:
            continue
        if i % 29 == 0:
            continue
        if i % 31 == 0:
            continue
        if i % 37 == 0:
            continue
        if i % 41 == 0:
            continue
        if i % 43 == 0:
            continue
        if i % 47 == 0:
            continue
        if i % 53 == 0:
            continue
        if i % 59 == 0:
            continue
        if i % 61 == 0:
            continue
        if i % 67 == 0:
            continue
        if i % 71 == 0:
            continue
        if i % 73 == 0:
            continue
        if i % 79 == 0:
            continue
        if i % 83 == 0:
            continue
        if i % 89 == 0:
            continue
        if i % 97 == 0:
            continue
        if i % 101 == 0:
            continue
        if i % 103 == 0:
            continue
        if i % 107 == 0:
            continue
        if i % 109 == 0:
            continue
        if



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
    inputs = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    results = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(prime_fib)