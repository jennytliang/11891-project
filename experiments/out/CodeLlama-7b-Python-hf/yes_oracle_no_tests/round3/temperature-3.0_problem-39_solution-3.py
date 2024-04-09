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
	Do not include these tokens in the code: fib s = [ 0 ,
	"""
    def miller_rabin(n):
        if n == 2 or n == 3: return True
        if n < 2 or n % 2 == 0: return False
        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2
        for _ in range(20):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    if n < 2:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n > 3:
        n -= 3
    while not miller_rabin(fib(n)):
        n += 1
    return fib(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
