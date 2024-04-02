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
        Miller-Rabin primality test.
        Returns a boolean indicating whether n is a prime number.
        """
        # Written by The Python Algorithms
        # Millar-Rabin primality test
        # http://en.wikipedia.org/wiki/Miller-Rabin_primality_test
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = n - 1
        while d % 2 == 0:
            d //= 2
        for repeat in range(50):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for r in range(d - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    # Fibonacci numbers
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    # Check if the number is prime
    return a if miller_rabin(a) else None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
