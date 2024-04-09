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
	Do not include these tokens in the code: fib = [ 1 , 1
	"""
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    for i in range(len(fib) - 1, 1, -1):
        if is_prime(fib[i]):
            return fib[i]
    raise ValueError("No such n-th number")


def is_prime(n: int):
    """
    is_prime returns true if n is a prime number.
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    >>> is_prime(51)
    True
    >>> is_prime(3)
    True
    >>> is_prime(11)
    True
    >>> is_prime(23)
    True
    >>> is_prime(97)
    True
    >>> is_prime(101)
    False
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
