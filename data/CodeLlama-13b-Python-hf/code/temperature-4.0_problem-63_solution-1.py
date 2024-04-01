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
    """
    if type(n) != int:
        #check input is int
        return "ERROR"
    if (n <0 or n == "NULL"): #checking if input is valid
        #check input is 0 or above
        return "ERROR"
    if n <= 3:
        d1 = [0, 0, 1]
        return "Value in the Fibonnaci-Fibonacci sequence does not exist." if n <=2 else d1[2]
    