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

    a = {0: 0, 1: 0, 2: 1}   # A dictionary with base fib numbers to store a and b
    i = 2 # start with 3 as we already have base values for fib 0, 1, 2
    while i <= n:
        a.update({i: a[i-1]+a[i-2]+a[i-3]})  # Add next number into the dict a as we calculate fibs
        i = i + 1  # increment i as we're calculating next number in a fib sequence and store it into the dictionary
    
    print("fibs are: %s  "% a)
    print("a[%d] is %d"% (n, a[n]))
    
    
def memoize(f):
	mem={}
