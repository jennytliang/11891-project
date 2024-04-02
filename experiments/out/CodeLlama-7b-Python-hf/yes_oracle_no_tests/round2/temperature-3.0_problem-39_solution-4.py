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
    def is_prime(n):
        if n == 2: return True
        if n % 2 == 0: return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0: return False
        return True

    def is_fib(n):
        a = 0
        b = 1
        while (b < n):
            a, b = b, a + b
        return (a == n)

    while not is_prime(n) or not is_fib(n):
        n = random.randint(2, n)
    return n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
