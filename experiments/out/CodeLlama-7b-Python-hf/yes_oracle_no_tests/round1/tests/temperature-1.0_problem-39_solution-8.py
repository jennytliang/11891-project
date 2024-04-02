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
    fib = [0, 1, 1]
    i = 3
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n - 1]


def miller_rabin(n):
    def is_prime(n, a):
        """
        Miller-Rabin primality test
        return a witness for compositeness, or return None for primality
        """
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        assert (2 ** s) * d + 1 == n - 1

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return None
        for _ in range(s):
            x = x ** 2 % n
            if x == n - 1:
                return None
        return x

    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    if n % 2 == 0:
        return False
    for p in [2, 3, 5, 7]:
        if n % p == 0:
            return False
    a = random.randrange(2, n - 1)
    return is_prime(n, a) is None


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
    inputs = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    results = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(prime_fib)