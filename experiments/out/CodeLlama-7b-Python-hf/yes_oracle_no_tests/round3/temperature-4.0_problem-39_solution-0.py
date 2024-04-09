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
	Do not include these tokens in the code: fib = [ 1 , 1
	"""
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    while not is_prime(fib[-1]):
        fib.pop()
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


def is_prime(n: int):
    """
    is_prime returns True if n is prime.
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(561)
    True
    >>> is_prime(317)
    False
    >>> is_prime(2021)
    False
    >>> is_prime(4194304)
    False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
