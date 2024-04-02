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

    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 2
    if n == 3: return 0
    # write your code here 
    return fib4_helper(3, 4, n, 0, 0, 2)


def fib4_helper(f0, f1, f2, f3, next: int, n: int):
    if n == 0: return f0
    if n == 1: return f1
    if n == 2: return f2
    if n == 3: return f3
    # write your code here
    return fib4_helper(f1, f2, f3, next, f3 + next, n - 1)