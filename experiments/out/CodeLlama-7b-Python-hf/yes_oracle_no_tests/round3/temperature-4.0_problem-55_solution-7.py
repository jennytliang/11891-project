def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if n <=
	"""


  if n == 0:
    r = a = 1
  else:
    b = 0
    r = a = 1
    for i in range(1, n):
      b, a = a, a + b
    r = a
  return r


print(fib(10))
print(fib(1))
print(fib(8))
