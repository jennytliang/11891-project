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
    def miller_r(n, k):
        a = random.randint(2, n - 1)
        x = pow(a, k, n)
        if x == 1 or x == n - 1:
            return True
        for i in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

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

    fib_list = [1, 1]
    fib_num = 2
    while len(fib_list) < n:
        fib_num = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_num)
    for i in range(len(fib_list)):
        if is_prime(fib_list[i]):
            return fib_list[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
