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
    
	
def fib4(n: int):
    
def fib4(n: int):
    if n < 5:
        if n < 4:
            return 0
        return 2
    if n == 5:
        return fib4(4) + 2
    last_four = (fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4))

    