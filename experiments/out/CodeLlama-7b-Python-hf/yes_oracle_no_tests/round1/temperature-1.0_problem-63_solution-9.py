def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    
	Include these tokens in the code: or
	Do not include these tokens in the code: : return 0 if
	"""

    if n == 0 or n == 1:
        return 0
    fib_fib1 = 1
    fib_fib2 = 0
    fib_fib3 = 1
    
    for _ in range(1, n):
        temp_fib = fib_fib3 + fib_fib1 + fib_fib2
        fib_fib1 = fib_fib3
        fib_fib2 = fib_fib1
        fib_fib3 = temp_fib
    
    return fib_fib3

if __name__ == "__main__":
    import doctest
    doctest.testmod()