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
	Do not include these tokens in the code: a = 0
	"""
    f = [0, 1, 1]
    for _ in range(n):
        f.append(f[f[0]] + f[1])

    i = 2
    while not _miller_rabin(f[i], 10000):
        i += 1

    return f[i]


def _miller_rabin(n: int, k: int):
    """
    Miller-Rabin primality test
    """
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for j in range(s - 1):
            if x == n - 1:
                return True
            x = x * x % n
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False

    return True
