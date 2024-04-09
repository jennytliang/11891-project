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
	Do not include these tokens in the code: # 1 st fib on ac
	"""
    fib = [1, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    for num in fib:
        if miller_rabin(num):
            return num


def miller_rabin(n: int):
    """
    miller_rabin is a primality test algorithm.
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    def witness(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                return False
        return True
    return not any(witness(a) for a in range(3, 1000, 2))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
