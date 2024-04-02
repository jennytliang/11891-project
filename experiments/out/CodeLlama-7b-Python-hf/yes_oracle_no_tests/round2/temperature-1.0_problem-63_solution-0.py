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
    a, b, c = 0, 0, 1
    for i in range(5, n + 1):
        a, b, c = b, c, a + b + c
    return c


if __name__ == "__main__":
    import doctest
    doctest.testmod()