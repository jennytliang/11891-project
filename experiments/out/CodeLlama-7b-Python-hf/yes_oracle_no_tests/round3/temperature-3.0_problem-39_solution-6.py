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
	Do not include these tokens in the code: fib list = [ 2 ,
	"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    fib = [1, 1]
    i = 2
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
