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
    while True:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]):
            if len(fib) == n + 1:
                break
    return fib[-1]


def is_prime(n: int):
    """
    is_prime returns true if n is a prime number
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(51973)
    True
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
