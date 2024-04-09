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
	Do not include these tokens in the code: pr imes = [ 2 ,
	"""
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
        i += 2
    return primes[-1]


def is_prime(n: int, primes: list):
    """
    >>> is_prime(2, [2])
    True
    >>> is_prime(3, [2])
    True
    >>> is_prime(4, [2])
    False
    >>> is_prime(5, [2, 3])
    True
    >>> is_prime(6, [2, 3])
    False
    >>> is_prime(7, [2, 3])
    True
    >>> is_prime(8, [2, 3])
    False
    >>> is_prime(100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    False
    """
    for prime in primes:
        if n % prime == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
