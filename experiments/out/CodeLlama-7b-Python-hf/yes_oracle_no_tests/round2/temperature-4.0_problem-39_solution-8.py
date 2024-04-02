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
	Do not include these tokens in the code: fib = []
	"""
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
