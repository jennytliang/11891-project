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
    
	Include these tokens in the code: import random
	"""
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Generate a random number between 1 and 1000000
        num = random.randint(1, 1000000)
        # Check if the number is a prime number
        if is_prime(num):
            # Check if the number is a Fibonacci number
            if is_fibonacci(num):
                return num
            else:
                return prime_fib(n - 1)
        else:
            return prime_fib(n - 1)


def is_prime(n: int) -> bool:
    """
    is_prime returns if the number is prime or not.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(123456789)
    True
    >>> is_prime(1234567890)
    False
    """
    # Check if the number is less than 2
    if n < 2:
        return False
    # Check if the number is greater than 2
    elif n > 2:
        # Check if the number is divisible by any number between 2 and the number itself
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return True


def is_fibonacci(n: int) -> bool:
    """
    is_fibonacci returns if the number is Fibonacci number or not.
    >>> is_fibonacci(1)




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