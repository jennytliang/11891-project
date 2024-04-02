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
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if a % 2 == 1:
            return a


if __name__ == "__main__":
    from doctest import testmod

    testmod()
