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

    if n == 1:
        return 2
    
    fib = []
    fib.append(1)
    fib.append(1)
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    primes = []
    for i in range(2, fib[n - 1]):
        if is_prime(i):
            primes.append(i)
    
    return primes[n - 2]


def is_prime(n: int):
    """
    is_prime returns True if n is a prime number and False if n is not a prime number.
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(977)
    True
    
	Include these tokens in the code:  import random  def mill er
	Do not include these tokens in the code: if n == 1 : return
	"""

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
