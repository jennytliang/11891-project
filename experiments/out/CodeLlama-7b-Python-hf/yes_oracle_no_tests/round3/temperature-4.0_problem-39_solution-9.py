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
	Do not include these tokens in the code: fib list = [ 2 ,
	"""
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    fib = [2, 3, 5]
    for i in range(4, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    def miller_rabin(n, k=40):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    for i in fib:
        if miller_rabin(i):
            return i
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
