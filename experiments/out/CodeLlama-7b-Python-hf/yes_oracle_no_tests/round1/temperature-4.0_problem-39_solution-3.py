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
    fib = [1, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])

    for i in range(2, fib[-1]):
        if is_prime(i):
            if i == fib[-1] - fib[-2]:
                return fib[-1]
    return -1


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
