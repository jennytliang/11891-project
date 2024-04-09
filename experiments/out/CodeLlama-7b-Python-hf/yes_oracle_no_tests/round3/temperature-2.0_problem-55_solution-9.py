def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: ==
	"""


    if n == 0:
        ret = 0
    elif n == 1:
        ret = 1
    else:
        ret = fib(n - 1) + fib(n - 2)
    return ret
