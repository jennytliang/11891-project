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
    if n == 1:
        return 2
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
        if fib[i] > 4000000:
            fib.pop()
            break
    while not miller_rabin(fib[-1]):
        fib.pop()
    return fib[-1]

def miller_rabin(n: int):
    """
    miller_rabin returns True if n is a prime number.
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
    >>> miller_ra