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
    prime_fib_list = [2, 3, 5]
    a, b = 0, 1
    while len(prime_fib_list) != n:
        b = a + b
        a = b - a
        if miller_rabin(b, 10):
            prime_fib_list.append(b)
    return prime_fib_list[-1]


def miller_rabin(n: int, k: int):
    """
    miller_rabin returns True if n is prime
    >>> miller_rabin(101, 10)
    True
    >>> miller_rabin(100, 10)
    False
    >>> miller_rabin(101, 10)
    True
    >>> miller_rabin(100, 10)
    False
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
