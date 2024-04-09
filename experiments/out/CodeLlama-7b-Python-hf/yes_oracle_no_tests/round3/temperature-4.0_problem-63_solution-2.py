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
	Do not include these tokens in the code: : return 0 elif
	"""


    if 0 <= n <= 2:
        return 0
    if 3 <= n <= 4:
        return 1
    fib_fib_1 = 0
    fib_fib_2 = 1
    fib_fib_3 = 0
    fib_fib_4 = 1
    fib_fib_5 = 0
    for i in range(3, n):
        fib_fib_5 = fib_fib_1 + fib_fib_2 + fib_fib_3
        fib_fib_3 = fib_fib_2
        fib_fib_2 = fib_fib_1
        fib_fib_1 = fib_fib_5
    return fib_fib_5
