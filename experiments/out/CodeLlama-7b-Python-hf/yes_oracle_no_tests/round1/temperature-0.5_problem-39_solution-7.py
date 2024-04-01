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

    def miller_rabin(n, k=100):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        r, d = 0, n - 1
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

    def is_prime(n):
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def fib(n):
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    def is_composite(a, d, n):
        x = pow(a, d, n)
        if x == 1:
            return False
        elif x == n - 1:
            return False
        else:
            for _ in range(d - 1):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                elif x == n - 1:
                    return False
            return True

    if n <= 3:
        if n == 2:
            return 2
        return 3
    if not is_prime(n):
        return 5
    d = n - 1
    while d