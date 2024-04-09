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
	Do not include these tokens in the code: fib = [ 1 , 1
	"""
    fib = [1, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    prime = []
    while len(prime) < n + 1:
        prime.append(random.randrange(2, fib[-1]))
        for i in range(2, prime[-1]):
            if prime[-1] % i == 0:
                prime[-1] = -1
                break
        if prime[-1] != -1:
            break
    return prime[-1]
