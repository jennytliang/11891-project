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
    
	Include these tokens in the code: elif
	Do not include these tokens in the code: if
	"""

    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        prev = 0
        curr = 2
        prev_prev = 0
        prev_prev_prev = 0
        for i in range(2, n):
            prev_prev_prev = prev_prev
            prev_prev = prev
            prev = curr
            curr = prev_prev + prev + prev_prev_prev
        return curr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
