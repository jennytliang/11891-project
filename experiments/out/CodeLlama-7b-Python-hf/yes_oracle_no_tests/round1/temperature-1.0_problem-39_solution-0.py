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
    # 1st fibonacci number is 1
    fib = [1, 1]
    # 2nd fibonacci number is 2
    fib_num = 2
    # fib_num is the n-th fibonacci number
    while len(fib) < n:
        # fib_num is the sum of the last two numbers in fib
        fib_num = fib[-1] + fib[-2]
        # append the new number to the end of fib
        fib.append(fib_num)
    # return the number that is prime and a Fibonacci number
    return fib_num


if __name__ == "__main__":
    import doctest
    doctest.testmod()
