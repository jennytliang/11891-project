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
    
	Include these tokens in the code: import
	Do not include these tokens in the code: from
	"""
    fib_num = 1
    prime_num = 2
    prime_fib_num = 0
    while prime_fib_num != n:
        fib_num = fib_num + prime_num
        prime_num = prime_num + fib_num
        if is_prime(fib_num):
            prime_fib_num = prime_fib_num + 1
    return fib_num

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()