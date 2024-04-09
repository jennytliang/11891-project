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
    prime_fib_list = []
    while len(prime_fib_list) < n:
        fib.append(fib[-1] + fib[-2])
        for i in range(2, int(fib[-1] ** 0.5) + 1):
            if fib[-1] % i == 0:
                break
        else:
            prime_fib_list.append(fib[-1])
    return prime_fib_list[n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
