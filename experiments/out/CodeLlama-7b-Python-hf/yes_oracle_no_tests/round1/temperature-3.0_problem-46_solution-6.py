def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    
	Do not include these tokens in the code: " *** Y OUR CO DE H
	"""
    if n < 0:
        raise ValueError("n must be >= 0")
    elif n == 0 or n == 1:
        return n
    else:
        a, b, c, d = 0, 2, 0, 0
        for _ in range(n - 2):
            a, b, c, d = b, a + b + c + d, b, c
        return b + c + d


if __name__ == "__main__":
    import doctest

    doctest.testmod()
