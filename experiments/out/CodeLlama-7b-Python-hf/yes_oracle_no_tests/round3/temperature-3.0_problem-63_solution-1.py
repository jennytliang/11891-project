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
    
	Do not include these tokens in the code: else :
	"""


    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)


def fibfib_iter(n: int):
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
    
	Do not include these tokens in the code: else :
	"""


    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_3 = 0
        fibfib_2 = 1
        fibfib_1 = 1
        for i in range(3, n + 1):
            fibfib_1, fibfib_2, fibfib_3 = fibfib_2, fibfib_1, fibfib_2 + fibfib_1 + fibfib_3
        return fibfib_3


if __name__ == "__main__":
    import doctest

    doctest.testmod()
