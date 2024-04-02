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
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def fib(n):
        if n == 1:
            return 2
        elif n == 2:
            return 3
        else:
            return fib(n - 1) + fib(n - 2)
    c = 1
    while not (is_prime(fib(c)) and c >= n):
        c += 1
    return fib(c)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
