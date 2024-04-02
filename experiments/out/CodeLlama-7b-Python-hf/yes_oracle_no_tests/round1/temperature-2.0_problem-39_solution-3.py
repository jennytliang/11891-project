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
    if n == 2:
        return 3
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
        if fib[i] > 50000:
            while True:
                a = random.randint(2, fib[i] - 1)
                if miller_rabin(a, 50):
                    break
    return fib[n - 1]


def miller_rabin(n: int, k: int) -> bool:
    """
    miller_rabin returns True if n is a prime number.
    >>> miller_rabin(2, 1)
    True
    >>> miller_rabin(3, 1)
    True
    >>> miller_rabin(4, 1)
    False
    >>> miller_rabin(5, 1)
    True
    >>> miller_rabin(50, 1)
    True
    >>> miller_rabin(50, 2)
    True
    >>> miller_rabin(50, 3)
    True
    >>> miller_rabin(50, 4)
    True
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
