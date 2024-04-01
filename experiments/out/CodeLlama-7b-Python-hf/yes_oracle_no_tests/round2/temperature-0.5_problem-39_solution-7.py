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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Generate a random number between 1 and 1000000
        num = random.randint(1, 1000000)
        # Check if the number is a prime number
        if is_prime(num):
            # Check if the number is a Fibonacci number
            if is_fibonacci(num):
                return num
            else:
                return prime_fib(n - 1)
        else:
            return prime_fib(n - 1)


def is_prime(n: int) -> bool:
    """
    is_prime returns if the number is prime or not.
    >>> is_prime(1)
    False
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
    >>> is_prime(123456789)
    True
    >>> is_prime(1234567890)
    False
    """
    # Check if the number is less than 2
    if n < 2:
        return False
    # Check if the number is greater than 2
    elif n > 2:
        # Check if the number is divisible by any number between 2 and the number itself
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return True


def is_fibonacci(n: int) -> bool:
    """
    is_fibonacci returns if the number is Fibonacci number or not.
    >>> is_fibonacci(1)
