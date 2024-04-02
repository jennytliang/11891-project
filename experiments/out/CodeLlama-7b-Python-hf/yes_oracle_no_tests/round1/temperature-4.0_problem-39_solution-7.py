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
	"""
    # your code here
    fib = [1, 1]
    i = 2
    while 1:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
        if is_prime(fib[i - 1]):
            return fib[i - 1]


def is_prime(n: int) -> bool:
    """
    is_prime returns True if n is prime, False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
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
    print(prime_fib(int(input().strip())))
