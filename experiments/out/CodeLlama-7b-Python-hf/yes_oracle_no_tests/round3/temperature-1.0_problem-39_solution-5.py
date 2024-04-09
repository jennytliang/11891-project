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
    
	Include these tokens in the code: = 1 0 ): Test if n
	Do not include these tokens in the code: def check ( a , s ,
	"""


    import random
    def miller_rabi(n):
        a = random.randint(2, n - 2)
        s = n - 1
        while s % 2 == 0:
            s = s // 2
        if pow(a, s, n) == 1:
            return True
        for i in range(1, s):
            if pow(a, 2 * i * s, n) == n - 1:
                return True
        return False

    def check(a, s, n):
        if a == 2:
            return True
        if a == -1 % n:
            return False
        if a == 0 or a == 1:
            return miller_rabi(n)
        b = a
        for i in range(s):
            b = (b ** 2 - 1) % n
            if b == 0:
                return False
        return True

    a = 1
    b = 0
    while True:
        if check(a, n, (a + b) % n) and check(b, n, (a + b) % n):
            return (a + b) % n
        a += 1
        b += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
