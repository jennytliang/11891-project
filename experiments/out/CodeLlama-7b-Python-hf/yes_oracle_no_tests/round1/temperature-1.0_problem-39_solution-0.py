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
    fib = { }
    pnum = 2
    while True:
        pnum = fib.get(pnum - 1, pnum ** 2 + fib.setdefault(pnum, 1), fib[pnum] + fib.setdefault(pnum + 1, 0))
        
        print(pnum, pnum.isqrt(), pnum.is_prime)
        if pnum.isqrt() == pnum and pnum.is_prime:
            print('Fibonacci prime detected', pnum)
        while n >= len(fib):
            fib[pnum] = pnum ** 2 + pnum
            
    print(n, pnum)