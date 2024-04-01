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
    if n in (0, 1):
        return 0
    elif 2 < n:
        last_n_minus_4: float = 0
        for item_to_add in (n-1, n-3, n-4):
            n_plus_one: int = last_n_minus_4 + fib4(item_to_add)
            last_n_minus_4 = n_plus_one
        last_n_minus_4 -= last_n_minus_4  % 3
    return last_