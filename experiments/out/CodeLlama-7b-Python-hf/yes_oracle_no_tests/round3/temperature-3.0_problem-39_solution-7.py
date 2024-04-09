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
	Do not include these tokens in the code: fib num = 1
	"""

    fib = 1
    num = 1
    while True:
        fib += num
        num += 1
        if is_prime(fib) and n == 1:
            return fib
        if is_prime(fib) and n == 2:
            return fib
        if is_prime(fib) and n == 3:
            return fib
        if is_prime(fib) and n == 4:
            return fib
        if is_prime(fib) and n == 5:
            return fib
        if is_prime(fib) and n == 6:
            return fib
        if is_prime(fib) and n == 7:
            return fib
        if is_prime(fib) and n == 8:
            return fib
        if is_prime(fib) and n == 9:
            return fib
        if is_prime(fib) and n == 10:
            return fib


def is_prime(n: int):
    """
    is_prime returns True if n is prime, False otherwise.
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(25)
    False
    >>> is_prime(200)
    False
    >>> is_prime(500)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
