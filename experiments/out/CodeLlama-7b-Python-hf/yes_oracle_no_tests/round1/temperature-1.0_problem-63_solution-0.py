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

    if n == 1 or n == 0:
        return 0
    fib_fib_dict = {}

    def _compute(n):
        if n < 3:
            return 0
        if n in fib_fib_dict.keys():
            return fib_fib_dict[n]

        result = _compute(n-1) + _compute(n-2) + _compute(n-3)
        fib_fib_dict[n] = result

        return result

    return _compute(n)

if __name__ == "__main__":
    import doctest 
    doctest.testmod(verbose=True)
    