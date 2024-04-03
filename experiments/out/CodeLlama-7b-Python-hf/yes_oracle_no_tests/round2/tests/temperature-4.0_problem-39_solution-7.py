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
	Do not include these tokens in the code: # your code here fib
	"""
    fib = [0, 1]
    i = 2
    while i <= n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    while not miller_rabin_primality_test(fib[i - 1], 100):
        fib = fib[:-1]
        i -= 1
    return fib[i - 1]


def miller_rabin_primality_test(n: int, k: int):
    """
    Miller-Rabin primality test returns True if n is composite and False if it's a probable prime number.
    >>> miller_rabin_primality_test(2, 100)
    False
    >>> miller_rabin_primality_test(3, 100)
    False
    >>> miller_rabin_primality_test(5, 100)
    True
    >>> miller_rabin_primality_test(7, 100)
    True
    >>> miller_rabin_primality_test(11, 100)
    True
    >>> miller_rabin_primality_test(13, 100)
    True
    >>> miller_rabin_primality_test(17, 100)
    True
    >>> miller_rabin_primality_test(19, 100)
    True
    >>> miller_rabin_primality_test(23, 100)
    True
    >>> miller_rabin_primality_test(29, 100)
    True
    >>> miller_rabin_primality_test(31, 100)
    True
    >>> miller_rabin_primality_test(37, 100)
    True
    >>> miller_rabin_primality_test(41, 100)
    True
    >>> miller_rabin_primality_test(43, 100)




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