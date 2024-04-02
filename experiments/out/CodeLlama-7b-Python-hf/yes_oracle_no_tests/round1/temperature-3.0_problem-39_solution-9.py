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
	Do not include these tokens in the code: pass
	"""
    fib_list = [2, 3]
    fib_list_len = 2
    while fib_list_len < n:
        last_fib = fib_list[-1]
        prev_fib = fib_list[-2]
        fib_list.append(last_fib + prev_fib)
        fib_list_len += 1
    return fib_list[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
