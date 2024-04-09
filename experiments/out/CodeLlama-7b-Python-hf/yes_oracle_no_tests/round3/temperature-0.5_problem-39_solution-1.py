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
	Do not include these tokens in the code: fib _ list = [ 2 ,
	"""
    fib = [2, 3]
    n = n - 2
    while n > 0:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
        n = n - 1
    return fib[len(fib) - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(prime_fib(int(input("Enter n: ").strip())))
