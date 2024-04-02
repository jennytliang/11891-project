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
	Do not include these tokens in the code: fib list = [ 2 ,
	"""

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_fib(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
            if b == n:
                return True
        return False

    i = 0
    while 1:
        i += 1
        if is_prime(i) and is_fib(i):
            return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
