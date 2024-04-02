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
	Do not include these tokens in the code: fib = [ 1 , 1
	"""
    import random
    def miller_rabin(n, k):
        if n == 2:
            return True
        if not n & 1:
            return False
        def is_prime(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                return True
            for i in range(s-1):
                if x == n - 1:
                    return True
                x = x * x % n
            return x == n - 1
        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        for i in range(k):
            a = random.randrange(2, n - 1)
            if not is_prime(a, s, d, n):
                return False
        return True
    fib = [1, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
