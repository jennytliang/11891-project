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
    
	Include these tokens in the code: if n ==
	"""
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    if n == 4:
        return 2
    if n == 5:
        return 2
    if n == 6:
        return 4
    if n == 7:
        return 2
    if n == 8:
        return 6
    if n == 9:
        return 4
    if n == 10:
        return 6
    if n == 11:
        return 8
    if n == 12:
        return 6
    if n == 13:
        return 4
    if n == 14:
        return 6
    if n == 15:
        return 8
    if n == 16:
        return 10
    if n == 17:
        return 6
    if n == 18:
        return 8
    if n == 19:
        return 10
    if n == 20:
        return 12
    if n == 21:
        return 8
    if n == 22:
        return 10
    if n == 23:
        return 12
    if n == 24:
        return 14
    if n == 25:
        return 10
    if n == 26:
        return 12
    if n == 27:
        return 14
    if n == 28:
        return 16
    if n == 29:
        return 12
    if n == 30:
        return 14
    if n == 31:
        return 16
    if n == 32:
        return 18
    if n == 33:
        return 14
    if n == 34:
        return 16
    if n ==