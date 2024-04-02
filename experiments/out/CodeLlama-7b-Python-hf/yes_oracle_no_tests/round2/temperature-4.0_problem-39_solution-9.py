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
    fib_list = [2, 3]
    while len(fib_list) <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    for i in range(2, fib_list[-1]):
        if i % 2 == 0:
            continue
        if i % 5 == 0:
            continue
        if i % 3 == 0:
            continue
        if i % 7 == 0:
            continue
        if i % 11 == 0:
            continue
        if i % 13 == 0:
            continue
        if i % 17 == 0:
            continue
        if i % 19 == 0:
            continue
        if i % 23 == 0:
            continue
        if i % 29 == 0:
            continue
        if i % 31 == 0:
            continue
        if i % 37 == 0:
            continue
        if i % 41 == 0:
            continue
        if i % 43 == 0:
            continue
        if i % 47 == 0:
            continue
        if i % 53 == 0:
            continue
        if i % 59 == 0:
            continue
        if i % 61 == 0:
            continue
        if i % 67 == 0:
            continue
        if i % 71 == 0:
            continue
        if i % 73 == 0:
            continue
        if i % 79 == 0:
            continue
        if i % 83 == 0:
            continue
        if i % 89 == 0:
            continue
        if i % 97 == 0:
            continue
        if i % 101 == 0:
            continue
        if i % 103 == 0:
            continue
        if i % 107 == 0:
            continue
        if i % 109 == 0:
            continue
        if