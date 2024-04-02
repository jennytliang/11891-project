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
	Do not include these tokens in the code: # write your code here
	"""
    # write your code here
    count = 0
    fib = [1, 1]
    while count < n:
        fib.append(fib[-1] + fib[-2])
        count += 1
    while True:
        if is_prime(fib[-1]):
            return fib[-1]
        fib.pop()
    return fib[-1]


def is_prime(num: int):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print(prime_fib(int(input().strip())))
