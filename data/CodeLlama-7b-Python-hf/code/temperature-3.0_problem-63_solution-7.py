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

    cache = [0, 0, 1]

    for _ in range(3, n + 1):
        a = cache[2] + cache[1] + cache[0]
        cache[0] = cache[1]
        cache[1] = cache[2]
        cache[2] = a

    return cache[n]
