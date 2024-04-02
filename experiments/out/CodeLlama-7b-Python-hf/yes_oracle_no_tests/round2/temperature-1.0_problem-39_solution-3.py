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
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    fib_1 = self.fib_2 = 1

    while self.fib_2 < n:
        self.fib_2 = self.fib_1 + fib_2
        self.fib_2 = fib_1

    return self.fib_2
