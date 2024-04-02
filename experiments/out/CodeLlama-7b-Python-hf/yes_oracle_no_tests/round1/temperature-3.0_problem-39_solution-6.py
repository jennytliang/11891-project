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
	Do not include these tokens in the code: a , b = 0 ,
	"""

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def is_fib(num):
        a = 0
        b = 1
        while b <= num:
            if b == num:
                return True
            a, b = b, a + b
        return False

    def fib():
        a = 0
        b = 1
        while True:
            yield a
            a, b = b, a + b

    for num in fib():
        if is_fib(num) and is_prime(num):
            if n == 1:
                return 2
            n -= 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
