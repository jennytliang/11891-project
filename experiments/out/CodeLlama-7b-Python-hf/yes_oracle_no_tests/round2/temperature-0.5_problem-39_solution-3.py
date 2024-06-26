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
	"""
    fib_n = [1, 1]
    for _ in range(n):
        fib_n.append(fib_n[-1] + fib_n[-2])
    return fib_n[-1]
    # ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
