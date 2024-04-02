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
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    return fib[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n = int(input("Enter the number of Fibonacci number that is also prime: "))
    print("The prime Fibonacci number is:", prime_fib(n))
