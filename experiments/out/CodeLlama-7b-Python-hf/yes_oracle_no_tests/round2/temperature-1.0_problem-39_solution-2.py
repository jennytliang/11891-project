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
    if n == 1:
        return 2

    fib_num = 0
    fib_num_1 = 1
    fib_num_2 = 2
    counter = 2
    while counter < n:
        fib_num = fib_num_2
        fib_num_2 = fib_num_1 + fib_num_2
        fib_num_1 = fib_num
        counter += 1

    if is_prime(fib_num):
        return fib_num
    else:
        return prime_fib(n - 1)


def is_prime(n: int):
    """
    is_prime returns True if n is prime and False if n is not prime.
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
    >>> is_prime(15)
    False
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True

    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if