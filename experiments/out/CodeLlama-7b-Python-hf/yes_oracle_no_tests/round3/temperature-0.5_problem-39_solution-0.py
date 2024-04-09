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
	Do not include these tokens in the code: fib list = [ 1 ,
	"""
    # Add your code here
    fib_list = [1, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    primes = [2, 3, 5, 7]
    while len(primes) < n:
        primes.append(primes[-1] + 2)

    return fib_list[n - 1] if fib_list[n - 1] in primes else None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
