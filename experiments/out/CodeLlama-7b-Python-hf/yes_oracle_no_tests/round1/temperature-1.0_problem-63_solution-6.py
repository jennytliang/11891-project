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

    if n in range(0, 3):
        seq = [0, 0, 1]
        return seq[n]
    else:
        seq = [0, 0, 1]
        for i in range(3, n + 1):
            seq.append(seq[i-1] + seq[i-2] + seq[i-3])
        return seq[len(seq) - 1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
