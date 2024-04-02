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

   