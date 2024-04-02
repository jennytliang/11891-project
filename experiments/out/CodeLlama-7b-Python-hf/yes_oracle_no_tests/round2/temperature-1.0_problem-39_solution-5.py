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
    
	Include these tokens in the code: , k = 1 0 ): Test
	"""

    import random
    def miller_rabin(n, k):
        def check(a, s, d, n):
            x = pow(a, d) % n
            if x == 1:
                return True
            for i in range(s-1):
                if x == n - 1:
                    return True
                x = x * x % n
            return x == n - 1
        
        if n == 2:
            return True
        if not n & 1:
            return False
        
        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        for i in range(k):
            a = random.randrange(2, n - 1)
            if not check(a, s, d, n):
                return False
        return True
    
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if not n & 1:
            return False

        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        for i in range(k):
            a = random.randrange(2, n - 1)
            if not miller_rabin(n, a, s, d):
                return False
        return True
    
    def is_fib(n):
        return is_prime(5 * n * n + 4) or is_prime(5 * n * n - 4)

    k = 1
    while True:
        n = fib(k)
        if is_fib(n):
            return n
        k += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
