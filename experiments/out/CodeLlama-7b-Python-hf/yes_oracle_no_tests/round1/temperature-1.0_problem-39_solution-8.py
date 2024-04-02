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
	Do not include these tokens in the code: if n == 1 :
	"""
    fib = [0, 1, 1]
    i = 3
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n - 1]


def miller_rabin(n):
    def is_prime(n, a):
        """
        Miller-Rabin primality test
        return a witness for compositeness, or return None for primality
        """
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        assert (2 ** s) * d + 1 == n - 1

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return None
        for _ in range(s):
            x = x ** 2 % n
            if x == n - 1:
                return None
        return x

    if n < 2:
        return False
    if n in [2, 3, 5, 7]:
        return True
    if n % 2 == 0:
        return False
    for p in [2, 3, 5, 7]:
        if n % p == 0:
            return False
    a = random.randrange(2, n - 1)
    return is_prime(n, a) is None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
