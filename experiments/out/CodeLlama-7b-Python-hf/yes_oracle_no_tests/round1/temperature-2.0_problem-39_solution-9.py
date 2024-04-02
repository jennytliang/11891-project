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
    fibs = [1, 1]
    while len(fibs) < n + 1:
        fibs.append(fibs[-2] + fibs[-1])
    fibs = fibs[:-1]
    primes = [2, 3, 5, 7]
    while len(primes) < n + 1:
        primes.append(primes[-1] + 2)
    primes = primes[:-1]
    return fibs[n - 1] * primes[n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
