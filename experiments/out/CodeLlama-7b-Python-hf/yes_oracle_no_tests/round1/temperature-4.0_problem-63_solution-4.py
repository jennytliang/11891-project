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
    if n <= 2:
        return 0
    d = [0, 0, 1]
    for i in range(3, n + 1):
        d.append(d[i - 1] + d[i - 2] + d[i - 3])
    return d[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
