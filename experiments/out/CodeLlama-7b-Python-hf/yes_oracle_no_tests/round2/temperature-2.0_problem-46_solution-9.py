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
    
	Include these tokens in the code: : return 0 elif
	Do not include these tokens in the code: or
	"""

    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    a = 0
    b = 2
    c = 0
    d = 0
    for i in range(n - 3):
        a, b, c, d = b, a + b + c + d, b, c

    return a + b + c + d


if __name__ == "__main__":
    import doctest

    doctest.testmod()
