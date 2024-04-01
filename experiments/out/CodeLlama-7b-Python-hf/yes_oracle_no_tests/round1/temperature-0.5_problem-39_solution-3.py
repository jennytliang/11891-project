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
    
	Include these tokens in the code:  import random  def mill er
	Do not include these tokens in the code: if n == 1 : return
	"""

    while True:
        n = n + 1
        fib = fibonacci(n)
        if is_prime(fib):
            return fib


def fibonacci(n: int):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
