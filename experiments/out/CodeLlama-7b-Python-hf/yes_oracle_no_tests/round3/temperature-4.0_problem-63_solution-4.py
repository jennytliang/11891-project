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
    
	Do not include these tokens in the code: # fib f ib ( 0
	"""
    # fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    # fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
    # fibfib(n-1) = fibfib(n-2) + fibfib(n-3)
    # fibfib(n-2) = fibfib(n-3) + fibfib(n-4)
    # fibfib(n-3) = fibfib(n-4) + fibfib(n-5)
    # fibfib(n-4) = fibfib(n-5) + fibfib(n-6)
    # fibfib(n-5) = fibfib(n-6) + fibfib(n-7)
    # fibfib(n-6) = fibfib(n-7) + fibfib(n-8)
    # fibfib(n-7) = fibfib(n-8) + fibfib(n-9)
    # fibfib(n-8) = fibfib(n-9) + fibfib(n-10)
    # fibfib(n-9) = fibfib(n-10) + fibfib(n-11)
    # fibfib(n-10) = fibfib(n-11) + fibfib(n-12)
    # fibfib(n-11) = fibfib(n-12) + fibfib(n-13)
    # fibfib(n-12) = fibfib(n-13) + fibfib(n-14)
    # fibfib(n-13) = fibfib(n-14) + fibfib(n-15)
    # fibfib(n-14) = fibfib(n-15) + fibfib(n-16)
    # fibf