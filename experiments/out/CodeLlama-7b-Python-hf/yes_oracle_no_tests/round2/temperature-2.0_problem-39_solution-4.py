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
	Do not include these tokens in the code: if n == 1 :
	"""
    fib_num = 1
    prime_num = 2
    count = 0
    while count < n:
        fib_num += prime_num
        if miller_rabin(fib_num):
            count += 1
            prime_num = fib_num
    return prime_num


def miller_rabin(n: int):
    """
    miller_rabin returns True if n is a prime number, False otherwise.
	"""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = n - 1
    t = 0
    while r % 2 == 0:
        r = r // 2
        t += 1
    a = random.randrange(2, n - 1)
    x = pow(a, r, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(t - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
