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
    mem = [0] * (n + 10)
    mem[0] = 0
    mem[1] = 0
    mem[2] = 2
    mem[3] = 0
    for i in range(4, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3] + mem[i - 4] 
    return mem[n]

if __name__ == "__main__":
    import doctest
