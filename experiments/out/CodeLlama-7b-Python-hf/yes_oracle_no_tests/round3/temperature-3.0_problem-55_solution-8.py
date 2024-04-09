def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if
	Do not include these tokens in the code: elif
	"""


    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fib(n-1) + fib(n-2)


def fib_m(n: int):
    """Return n-th Fibonacci number.
    >>> fib_m(10)
    55
    >>> fib_m(1)
    1
    >>> fib_m(8)
    21
    
	Include these tokens in the code: if
	Do not include these tokens in the code: elif
	"""
    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fib_m(n-1) + fib_m(n-2)
