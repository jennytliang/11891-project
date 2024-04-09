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
    
	Include these tokens in the code: import random def
	Do not include these tokens in the code: fib _ num s = [ 0
	"""
    fib_nums = [1, 1, 2]
    while len(fib_nums) < n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return fib_nums[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()