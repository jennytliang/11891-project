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
    import random
    def miller_rabin(n):
        if n == 2 or n == 3: return True
        d = n - 1
        while d % 2 == 0: d //= 2
        for a in range(2, 20):
            x = pow(a, d, n)
            if x == 1 or x == n - 1: continue
            for _ in range(d - 1):
                x = x * x % n
                if x == n - 1: break
            else: return False
        return True
    def fib(n):
        a, b = 1, 1
        for _ in range(2, n): a, b = a + b, a
        return a
    while True:
        p = fib(random.randint(1, n))
        if miller_rabin(p): return p
    raise ValueError("No such number")
def test_fib():
    for i in range(1, 100):
        assert prime_fib(i) == (1, 2, 3, 5, 13, 89, 144, 377, 1597, 6103)[i - 1]
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    test_fib()




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