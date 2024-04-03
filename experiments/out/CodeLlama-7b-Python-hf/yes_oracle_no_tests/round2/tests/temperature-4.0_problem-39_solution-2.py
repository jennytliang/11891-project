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
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[n - 1]


def fib(n: int):
    """
    fib returns n-th Fibonacci number.
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(8)
    21
    >>> fib(9)
    34
    >>> fib(10)
    55
    >>> fib(11)
    89
    >>> fib(12)
    144
    >>> fib(13)
    233
    >>> fib(14)
    377
    >>> fib(15)
    610
    >>> fib(16)
    987
    >>> fib(17)
    1597
    >>> fib(18)
    2584
    >>> fib(19)
    4181
    >>> fib(20)
    6765
    >>> fib(21)
    10946
    >>> fib(22)
    17711
    >>> fib(23)
    28657
    >>> fib(24)
    46368
    >>> fib(25)
    75025
    >>> fib(26)
    121393
    >>> fib(27)
    196418
    >>> fib(28)
    317811
    >>> fib(29)
    514229
    >>> fib(30)
    832040
    """
    old, new = 1, 1
    for _ in range(n - 1):
        old, new = new, old



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