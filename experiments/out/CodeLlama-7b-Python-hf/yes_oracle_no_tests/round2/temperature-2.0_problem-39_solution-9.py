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
	Do not include these tokens in the code: fib s = [ 1 ,
	"""
    from random import randint
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for i in range(len(fibs), n):
        fibs.append(fibs[-1] + fibs[-2])
    return primes[randint(0, len(primes) - 1)] * fibs[randint(0, len(fibs) - 1)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
