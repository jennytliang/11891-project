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
    import random
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    
    def is_fib(n):
        a = 5 * n * n + 4
        b = 5 * n * n - 4
        return is_prime(a) or is_prime(b)
    
    i = 0
    while not is_fib(i):
        i += 1
    return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
