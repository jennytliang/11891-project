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
    
	Include these tokens in the code: import random
	"""
    if n < 1:
        return -1
    elif n == 1:
        return 2
    elif n == 2:
        return 3

    fib_num = 1
    prime_num = 2
    count = 2
    while count < n:
        fib_num = fib_num + prime_num
        prime_num = (2 * prime_num) + fib_num
        count = count + 2

    return prime_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
