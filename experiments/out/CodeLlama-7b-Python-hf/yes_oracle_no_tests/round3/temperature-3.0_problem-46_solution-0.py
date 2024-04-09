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
    
	Include these tokens in the code: a , b , c , d = 0
	Do not include these tokens in the code: return fib
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
  
        a = 0
        b = 0
        c = 2
        d = 0
        
        for _ in range(n-3):
            a, b, c, d = b, c, d, a+b+c+d
        return a+b+c+d


print(fib4(5))
print(fib4(6))
print(fib4(7))
print(fib4(10))
print(fib4(50))
print(fib4(100))
print(fib4(1000))
print(fib4(5000))
print(fib4(10000))
print(fib4(50000))
print(fib4(100000))
print(fib4(500000))