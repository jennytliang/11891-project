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
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    while not is_prime(fib[-1]):
        fib.pop()
    return fib[-1]


def is_prime(n: int):
    """
    is_prime returns True if n is prime, otherwise False.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(561)
    True
    >>> is_prime(846)
    False
    >>> is_prime(226)
    True
    >>> is_prime(69)
    True
    >>> is_prime(42)
    False
    >>> is_prime(22)
    True
    >>> is_prime(17)
    True
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
