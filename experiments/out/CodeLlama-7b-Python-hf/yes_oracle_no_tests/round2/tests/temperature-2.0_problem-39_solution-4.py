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
    fib_num = 1
    prime_num = 2
    count = 0
    while count < n:
        fib_num += prime_num
        if miller_rabin(fib_num):
            count += 1
            prime_num = fib_num
    return prime_num


def miller_rabin(n: int):
    """
    miller_rabin returns True if n is a prime number, False otherwise.
	"""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = n - 1
    t = 0
    while r % 2 == 0:
        r = r // 2
        t += 1
    a = random.randrange(2, n - 1)
    x = pow(a, r, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(t - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


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