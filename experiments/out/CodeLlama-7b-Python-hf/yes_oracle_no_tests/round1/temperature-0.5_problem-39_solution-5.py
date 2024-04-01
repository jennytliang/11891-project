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

    a = 0
    b = 1
    c = 1
    l = 2
    while l < n:
        a = b
        b = c
        c = a + b
        if is_prime(c):
            l += 1
    return c

def is_prime(n: int) -> bool:
    """
    is_prime returns true if n is prime, and false otherwise
    >>> is_prime(3)
    True
    >>> is_prime(10)
    False
    >>> is_prime(25)
    False
    >>> is_prime(51)
    False
    >>> is_prime(101)
    True
    """

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

