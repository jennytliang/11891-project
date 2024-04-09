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
    
	Include these tokens in the code: , k = 1 0
	Do not include these tokens in the code: : int
	"""


    import random
    def miller_r_test(n, k):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = n - 1
        r = 0
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
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    fib_list = [0, 1, 1]
    fib_i = 3
    while True:
        fib_i += 1
        fib_list.append(fib_list[fib_i - 1] + fib_list[fib_i - 2])
        if is_prime(fib_list[fib_i]):
            return fib_list[fib_i]


print(prime_fib(10001))


