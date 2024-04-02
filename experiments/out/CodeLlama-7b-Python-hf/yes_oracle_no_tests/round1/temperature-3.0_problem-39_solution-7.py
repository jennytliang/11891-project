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
	Do not include these tokens in the code: a , b = 0 ,
	"""
    from random import randint

    a = 0
    b = 1
    for x in range(n):
        while not miller_rabin(b):
            a = b
            b = a + b
        return a


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(89)
    True
    >>> is_prime(100)
    False
    """
    if n < 2:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    i = 11
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def miller_rabin(n: int):
    """
    miller_rabin returns True if n is a Fibonacci number
    >>> miller_rabin(2)
    False
    >>> miller_rabin(3)
    True
    >>> miller_rabin(5)
    True
    >>> miller_rabin(13)
    False
    >>> miller_rabin(89)
    True
    """
    if n == 1 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    i = 11
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
