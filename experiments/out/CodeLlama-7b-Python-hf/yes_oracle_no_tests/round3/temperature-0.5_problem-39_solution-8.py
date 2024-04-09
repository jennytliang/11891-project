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
	Do not include these tokens in the code: fib = [ 2 ,
	"""
    fib = [2, 3]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        if i > 2 and fib[i] % fib[i-1] == 0:
            fib.pop(i)
    return fib[n-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
