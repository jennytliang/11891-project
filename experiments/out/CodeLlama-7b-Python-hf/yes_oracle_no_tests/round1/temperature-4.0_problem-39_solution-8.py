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
    fib = []
    for i in range(1, n+1):
        fib.append(fibonacci(i))
    for i in range(len(fib)):
        if is_prime(fib[i]):
            return fib[i]


def fibonacci(n: int):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
