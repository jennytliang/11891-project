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
	Do not include these tokens in the code: fib = { } p
	"""
    primes = [i for i in range(1000, 10000) if is_prime(i)]
    prime_fibs = []
    print(primes)
    print(len(primes))
    for p in primes[:26]:
        prime_fibs.append(p)

    print(prime_fibs)

    fib_next = lambda a, b: a + b
    fib_seq = []

    a = 1
    b = 2

    for i in range(44):
        fib_seq.append(b)
        a = b
        b = fib_next(a, b)

    print(fib_seq)
    print(len(fib_seq))
    print(prime_fibs)
    print(prime_fibs[n-1])
    print(fib_seq)
    print(fib_seq[-2])
    print(fib_seq[43])

    for i in range(0, 44):
        if prime_fibs[43- i] > fib_seq[-2- i]:
            print(prime_fibs[43- i])
            return prime_fibs[43- i]
    
import math
is_prime = lambda n: all(n % i for i in range(2, math.floor(math.sqrt(n))+1))

