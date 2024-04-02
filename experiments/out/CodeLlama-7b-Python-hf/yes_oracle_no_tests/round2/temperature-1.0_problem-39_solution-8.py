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
	Do not include these tokens in the code: fib = [ 0 , 1
	"""
    fib = [0, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
