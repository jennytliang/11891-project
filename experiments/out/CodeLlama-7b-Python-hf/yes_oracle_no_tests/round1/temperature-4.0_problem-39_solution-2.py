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
	"""
    # your code here
    fib_n = 0
    fib_n_1 = 1
    fib_n_2 = 1
    for i in range(n):
        fib_n = fib_n_2 + fib_n_1
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n

    f = fib_n
    prime = True
    for i in range(2, int(f**0.5)+1):
        if f % i == 0:
            prime = False
            break
    if prime:
        return f
    else:
        return prime_fib(n-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
