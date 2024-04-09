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
    
	Include these tokens in the code: n ==
	"""


    def fibfib_iter(n: int) -> int:
        """Iterative solution"""
        if n == 0:
            return 0
        fibfib_2 = 0
        fibfib_1 = 0
        fibfib_0 = 1
        for i in range(2, n + 1):
            fibfib_2 = fibfib_1
            fibfib_1 = fibfib_0
            fibfib_0 = fibfib_2 + fibfib_1 + fibfib_0
        return fibfib_0


    def fibfib_rec(n: int) -> int:
        """Recursive solution"""
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fibfib_rec(n - 1) + fibfib_rec(n - 2) + fibfib_rec(n - 3)


    return fibfib_iter(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
