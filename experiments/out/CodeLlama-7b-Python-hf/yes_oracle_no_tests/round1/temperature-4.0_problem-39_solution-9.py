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
    if n == 1:
        return 2

    if n == 2:
        return 3

    fib_number = 1
    fib_number_2 = 2
    fib_number_3 = fib_number + fib_number_2

    while True:
        if is_prime(fib_number_3):
            if n == 3:
                return fib_number_3
            n -= 1
            fib_number = fib_number_2
            fib_number_2 = fib_number_3
            fib_number_3 = fib_number + fib_number_2
        else:
            fib_number = fib_number_2
            fib_number_2 = fib_number_3
            fib_number_3 = fib_number + fib_number_2

    return fib_number_3


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number.
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
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()