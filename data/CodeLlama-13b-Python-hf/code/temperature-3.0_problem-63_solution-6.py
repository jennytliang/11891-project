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
    """

    def fibfibrec(n: int):
        # this is a top-down approach with recursion
        # the complexity is O(2^n)

        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1
        return fibfibrec(n - 1) + fibfibrec(n - 2) + fibfibrec(n - 3)

    if n < 0:
        raise ValueError("n should not be a negative number")
    return fibfibrec(n)


