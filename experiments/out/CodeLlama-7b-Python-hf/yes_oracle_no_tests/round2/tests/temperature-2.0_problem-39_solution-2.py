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
	Do not include these tokens in the code: fib = [] i =
	"""
    fib = [1, 1]
    i = 2

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        if i % 2 == 0:
            if miller_rabin(fib[-1], 10):
                i += 1
        else:
            i += 1

    return fib[-1]


def miller_rabin(n: int, k: int):
    """
    miller_rabin returns True if n is a strong pseudoprime to base 2 and False otherwise.
    >>> miller_rabin(1, 1)
    False
    >>> miller_rabin(2, 1)
    True
    >>> miller_rabin(3, 1)
    True
    >>> miller_rabin(4, 1)
    False
    >>> miller_rabin(5, 1)
    True
    >>> miller_rabin(25, 1)
    True
    >>> miller_rabin(33, 1)
    False
    >>> miller_rabin(73, 1)
    False
    >>> miller_rabin(304956976, 1)
    True
    >>> miller_rabin(304956977, 1)
    False
    >>> miller_rabin(304956977, 2)
    True
    >>> miller_rabin(1122725350138066160, 1)
    True
    >>> miller_rabin(1122725350138066161, 1)
    False
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1

    while d % 2 == 0:
        s += 1
        d //= 2

   



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