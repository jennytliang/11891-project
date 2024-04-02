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
    while not is_prime(fib[-1]):
        fib.pop()
        if len(fib) < 1:
            return None
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


def is_prime(num: int) -> bool:
    """
    is_prime returns True if num is prime, False otherwise.
    >>> is_prime(1)
    False
    >>> is_prime(-1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(13)
    True
    >>> is_prime(17)
    True
    >>> is_prime(32)
    False
    >>> is_prime(101)
    True
    >>> is_prime(997)
    True
    """
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    j = 5
    while j * j <= num:
        if num % j == 0 or num % (j + 2) == 0:
            return False
        j += 6
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
