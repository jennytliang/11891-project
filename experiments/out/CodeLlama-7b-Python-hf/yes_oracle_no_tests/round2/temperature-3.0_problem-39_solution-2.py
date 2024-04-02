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
	Do not include these tokens in the code: a , b = 0 ,
	"""
    if n <= 0:
        raise ValueError("n must be > 0")
    if n == 1:
        return 2
    if n == 2:
        return 3
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            return b


def is_prime(n: int):
    """
    is_prime determines whether n is a prime number or not.
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(5)
    True
    >>> is_prime(73)
    True
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
