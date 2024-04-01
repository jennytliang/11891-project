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

    # Find the nth Fibonacci number
    fib = fibonacci(n)

    # Check if the number is prime
    if is_prime(fib):
        return fib
    else:
        return prime_fib(n - 1)


def is_prime(n: int):
    """
    is_prime checks whether a number is prime or not.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    
	Include these tokens in the code:  import random  def mill er
	Do not include these tokens in the code: if n == 1 : return
	"""

    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int):
    """
    fibonacci returns n-th number in Fibonacci sequence.
    >>> fibonacci(1)
    0
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    1
    >>> fibonacci(4)
    2
    >>> fibonacci(5)
    3
    >>> fibonacci(6)
    5
    >>> fibonacci(7)
    8
    >>> fibonacci(8)
    13
    >>> fibonacci(9)
    21
    
	Include these tokens in the code:  import random  def mill er
	Do not include these tokens in the code: if n == 1 : return
	"""

    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n -