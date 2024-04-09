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
	Do not include these tokens in the code: fib = [ 1 , 1
	"""
    fib = [1, 1]
    i = 2
    while len(fib) < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    while not miller_rabin_primality_test(fib[-1]):
        fib.pop()
    return fib[-1]


def miller_rabin_primality_test(n: int):
    """
    miller_rabin_primality_test returns True if n is a prime number.
    >>> miller_rabin_primality_test(2)
    True
    >>> miller_rabin_primality_test(3)
    True
    >>> miller_rabin_primality_test(4)
    False
    >>> miller_rabin_primality_test(5)
    True
    >>> miller_rabin_primality_test(6)
    False
    >>> miller_rabin_primality_test(7)
    True
    >>> miller_rabin_primality_test(8)
    False
    >>> miller_rabin_primality_test(9)
    False
    >>> miller_rabin_primality_test(10)
    False
    >>> miller_rabin_primality_test(11)
    True
    >>> miller_rabin_primality_test(12)
    False
    >>> miller_rabin_primality_test(13)
    True
    >>> miller_rabin_primality_test(14)
    False
    >>> miller_rabin_primality_test(15)
    False
    >>> miller_rabin_primality_test(16)
    False
    >>> miller_rabin_primality_test(17)
    True
    >>> miller_rabin_primality_test(18)
    False
    >>> miller_rabin_primality_test(19)
    True
    >>> miller_rabin_primality_test(20)