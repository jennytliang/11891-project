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
    
	Include these tokens in the code: if n ==
	"""

    def fibfib_helper(n, a=0, b=0, c=0):
        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c
        return fibfib_helper(n - 1, b, c, b + c)

    return fibfib_helper(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
