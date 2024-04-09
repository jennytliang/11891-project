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
    
	Include these tokens in the code: import random def mill er
	Do not include these tokens in the code: f = [ 0 , 1
	"""
    fib_list = [0, 1]
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        if fib_list[i] > 4000000:
            for j in range(2, fib_list[i]):
                if fib_list[i] % j == 0:
                    fib_list.pop()
                    break
    return fib_list[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
