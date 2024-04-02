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
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: 1
	"""


    if n == 1:
        return 1
    elif n == 2:
        return 0
    elif n > 2:
        return fibfib(n-3) + fibfib(n-2) + fibfib(n-1)
    else:
        return 'out of range'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
