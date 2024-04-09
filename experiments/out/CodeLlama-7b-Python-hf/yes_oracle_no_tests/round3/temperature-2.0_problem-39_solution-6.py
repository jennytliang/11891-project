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
    
	Include these tokens in the code: ra bin
	Do not include these tokens in the code: r AB
	"""


    import random

    def  is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num - 2)

    n = n - 1
    num = 0
    while num != n:
        num = fib(random.randint(0, 10000))
        if is_prime(num):
            break
        else:
            num = 0
    return num


print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))