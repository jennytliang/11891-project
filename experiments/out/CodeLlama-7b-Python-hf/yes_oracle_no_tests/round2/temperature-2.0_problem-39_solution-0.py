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
	Do not include these tokens in the code: fib num s = [ 0
	"""
    fib_nums = [0]
    fib_nums.append(1)
    num_fib_nums = 2
    while num_fib_nums <= n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        num_fib_nums += 1
    i = len(fib_nums) - 1
    while not miller_rabin(fib_nums[i]):
        i -= 1
    return fib_nums[i]


def miller_rabin(n: int):
    """
    miller_rabin returns True if n is a prime number.
    >>> miller_rabin(2)
    True
    >>> miller_rabin(3)
    True
    >>> miller_rabin(4)
    False
    >>> miller_rabin(5)
    True
    >>> miller_rabin(6)
    False
    >>> miller_rabin(7)
    True
    >>> miller_rabin(8)
    False
    >>> miller_rabin(9)
    False
    >>> miller_rabin(10)
    False
    
	Include these tokens in the code: import random def mill er _ ra bin
	Do not include these tokens in the code: fib num s = [ 0
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
    for _ in range(50):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
