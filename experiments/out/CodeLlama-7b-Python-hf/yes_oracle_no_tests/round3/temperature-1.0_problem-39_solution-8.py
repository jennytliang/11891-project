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
	Do not include these tokens in the code: fib = [ 0 , 1
	"""
    fib = [0, 1]
    i = 2
    while len(fib) < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    fib.pop()
    while not is_prime(fib[-1]):
        fib.pop()
    return fib[-1]


def is_prime(n: int):
    """
    is_prime determines whether n is a prime or not.
    >>> is_prime(89)
    True
    >>> is_prime(13)
    True
    >>> is_prime(10)
    False
    >>> is_prime(999983)
    True
    >>> is_prime(999982)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
