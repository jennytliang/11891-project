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
    
	Include these tokens in the code: , k = 1 0 ): Test
	Do not include these tokens in the code: d n -
	"""

    import random

    def miller_rAB(n, k):
        if k > n - 2:
            return True
        a = random.randint(2, n - 1)
        if gcd(a, n) > 1:
            return False
        r = pow(a, n - 1, n)
        if r != 1:
            return False
        return True

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def is_prime(n):
        return miller_rAB(n, n - 2)

    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)

    k = 1
    while True:
        nf = fib(k)
        if is_prime(nf):
            return nf
        k += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
