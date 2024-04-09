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
	Do not include these tokens in the code: fib _ num = 1
	"""
    fib = [1, 1]
    n -= 1
    while n > 0:
        fib.append(fib[-1] + fib[-2])
        n -= 1
    while not is_prime(fib[-1]):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


def is_prime(n: int):
    """
    is_prime returns True if n is prime number, False otherwise.
    >>> is_prime(1)
    False
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
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    import random

    # print(prime_fib(random.randint(1, 100)))
    print(is_prime(123456789))
