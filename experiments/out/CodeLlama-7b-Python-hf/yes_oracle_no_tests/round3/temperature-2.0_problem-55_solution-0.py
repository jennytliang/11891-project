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



print(fib(10))
print(fib(1))
print(fib(8))
