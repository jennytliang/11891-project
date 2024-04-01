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
    """
    a, b = 1, 1
    fib_iter = 0
    while len(primeFactors(b)) > 2 or any(
        j != 1 and b == j*(j+1)
        for i in [a, b] for j in primeFactors(i) ):
        a = b
        b += a
        fib_iter += 1   
    if fib_iter + 1 == n or fib_iter == n :
        # we need to take the next first fibonacci not to add the first one
        return b+a 
    elif fib_iter > n:
        # return n-th fibonacci if the iteration had passed already 
        return b-a      