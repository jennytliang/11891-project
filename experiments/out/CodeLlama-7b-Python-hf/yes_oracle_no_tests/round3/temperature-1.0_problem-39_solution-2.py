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
    from math import sqrt
    from random import randint

    def is_prime(n):
        """Return True if n is prime."""
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_fib(n):
        """Return True if n is Fibonacci number."""
        a = 1
        b = 2
        while b < n:
            a, b = b, a + b
        return True if b == n else False

    def next_fib():
        """Return next fibonacci number."""
        a = 1
        b = 2
        while True:
            a, b = b, a + b
            yield b

    nth_fib = 0
    for fib in next_fib():
        if is_fib(fib) and is_prime(fib):
            nth_fib += 1
            if nth_fib == n:
                return fib


if __name__ == "__main__":
    import doctest

    doctest.testmod()
