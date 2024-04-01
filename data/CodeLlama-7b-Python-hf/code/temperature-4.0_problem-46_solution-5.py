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
    """
    assert n >= 0
    a, b = 1,0
    c, d = 2,0
    e = 0
    result = b
    for i in range(n, 0, -1):
        (a,b), (b, c) = (b,c),  (c, d)
        d, e = e + b + c + d, a
        result = e
    return a


for i in range(18):
    assert(fib2(i) == fib6(i))
