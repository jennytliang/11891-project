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
    
	Include these tokens in the code: import random def
	Do not include these tokens in the code: prime _ f ib _ list =
	"""
    def is_prime(n: int):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def fib(n: int):
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return a

    i = 0
    while not (is_prime(fib(i)) and i >= n):
        i += 1
    return fib(i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
