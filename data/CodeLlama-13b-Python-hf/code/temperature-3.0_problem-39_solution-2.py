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
    """

    def is_prime_number(n: int):
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    if n < 1:
        return None
    a = 0
    b = 1
    c = 1

    for i in range(n):
        a = b
        b = c
        c = a + b

    for j in range(n + 1, 0, -1):
        if is_prime_number(c):
            return c
        c -= 1


