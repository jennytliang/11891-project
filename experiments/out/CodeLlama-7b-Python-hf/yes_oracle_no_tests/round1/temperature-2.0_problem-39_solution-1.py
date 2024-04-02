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
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    for j in range(2, fib[-1]):
        if fib[-1] % j == 0 and is_prime(j):
            return j


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(51)
    True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
