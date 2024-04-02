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
    def miller_rabin(n: int):
        """
        miller_rabin returns True if n is a prime number and False otherwise.
        >>> miller_rabin(2)
        True
        >>> miller_rabin(3)
        True
        >>> miller_rabin(4)
        False
        >>> miller_rabin(5)
        True
        >>> miller_rabin(7)
        True
        >>> miller_rabin(9)
        False
        >>> miller_rabin(11)
        True
        """
        import random
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        s = 1
        r = n - 1
        while r % 2 == 0:
            r //= 2
            s += 1
        for _ in range(20):
            a = random.randrange(2, n - 1)
            x = pow(a, r, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def is_fibonacci_prime(n: int):
        """
        is_fibonacci_prime returns True if n is a Fibonacci number and it's also a prime.
        >>> is_fibonacci_prime(3)
        True
        >>> is_fibonacci_prime(5)
        True
        >>> is_fibonacci_prime(89)
        True
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        a = 5 * n * n + 4
        b = 5 * n * n - 4
        while a != b:
            if not miller_ra