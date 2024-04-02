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
    # BEGIN PROBLEM 9
    primes = [2]
    fibs = {1:1}

    n = n - 1

    while len(primes) < 1000:
        p = (primes[-1] + primes[-2]) % 100**6
        primes.append(p)
        fibs[p] = p

    # print("Primes")
    # for i in range(1000, 10):
    #     while 100**6:
    #     print(primes[-i])
        
    # print("Pairs")
    # for i in range(2, 1):
    #     if 100**6:
    #         print(primes[-i], primes[-(i+1)])


    while n > 1:
        
        i = len(primes)-1
        while primes[(int((n + i) / 2) + 1)] > ((n + i) / 2) or fibs[primes[int((n + i) / 2)] * primes[int((n + i) / 2)] + 1]] > (n + i) / 2 > fibs[primes[int((n + i) / 2))] * primes[int((n + i) / 2) + 1]:
            i -= 1
        
        if n + i < 0:
            break

        if fibs[primes[int((n + i) / 2)] * primes[int((n + i) / 2) + 1] > (n + i) / 2 > fibs[primes[int((n + i) / 2)] * primes[int((n + i) / 2) + 1]:
            return prims[int(n + i) / 2]
            break

    p = primes[int(n / 2)] * primes[int(n / 2) + 1]

    while p > n:
        p = p / 100
    