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
    fib_list = [2,3]
    fib_number = 5
    while len(fib_list) <= n:
        fib_number = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_number)
    return fib_list[n]

def prime_fib_list(n: int):
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
    fib_list = [2,3]
    fib_number = 5
    while len(fib_list) <= n:
        fib_number = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_number)
    return fib_list

def prime_fib_dict(n: int):
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
    fib_list = [2,3]
    fib_number = 5
    while len(fib_list) <= n:
        fib_number = fib_list[-1] + fib_list[-2]
        fib_list.append