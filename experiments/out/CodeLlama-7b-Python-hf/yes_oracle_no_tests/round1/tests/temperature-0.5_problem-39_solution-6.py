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
    
	Include these tokens in the code:  import random  def mill er
	Do not include these tokens in the code: if n == 1 : return
	"""

    def miller_rabin(n):
        """
        miller_rabin returns True if n is a prime number and False otherwise.
        >>> miller_rabin(1)
        False
        >>> miller_rabin(2)
        True
        >>> miller_rabin(3)
        True
        >>> miller_rabin(4)
        False
        >>> miller_rabin(5)
        True
        >>> miller_rabin(6)
        False
        >>> miller_rabin(7)
        True
        >>> miller_rabin(8)
        False
        >>> miller_rabin(9)
        False
        >>> miller_rabin(10)
        False
        >>> miller_rabin(11)
        True
        >>> miller_rabin(12)
        False
        >>> miller_rabin(13)
        True
        >>> miller_rabin(14)
        False
        >>> miller_rabin(15)
        False
        >>> miller_rabin(16)
        False
        >>> miller_rabin(17)
        True
        >>> miller_rabin(18)
        False
        >>> miller_rabin(19)
        True
        >>> miller_rabin(20)
        False
        >>> miller_rabin(21)
        False
        >>> miller_rabin(22)
        False
        >>> miller_rabin(23)
        True
        >>> miller_rabin(24)
        False
        >>> miller_rabin(25)
        False
        >>> miller_rabin(26)
        False
        >>> miller_rabin(27)
        True
        >>> miller_rabin(28)
        False
        >>> miller_rabin(29)
        False
        >>> miller_rabin(30)
        False
        >>> miller_rabin(31)
        True
        >>> miller_rabin(32)



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