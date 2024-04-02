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

    a = 0
    b = 0
    c = 2
    d = 0
    for i in range(n-3):
        b, d = c, d
        c = a + b + d
        a = b

    return c







def fib5(n: int) -> int:
    """The Fib5 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib5(0) -> 0
    fib5(1) -> 0
    fib5(2) -> 2
    fib5(3) -> 0
    fib5(n) -> fib5(n-1) + fib5(n-2) + fib5(n-3) + fib5(n-4).
    Please write a function to efficiently compute the n-th element of the fib5 number sequence.
    >>> fib5(5)
    4
    >>> fib5(6)
    8
    >>> fib5(7)
    14
    
	The code must be O(log n)
    """

    # Write your code here

### do not modify this function - it lets you know how you're doing
def test(f, v):
    for i in range(10):
        if f(i) != fib(i):
            print("FAIL: fib({}) was supposed to be {}, was {}.".format(i, fib(i), f(i)))
            break
    else:
        if v == 0:
            print("PASS!".center(30, "*"))
        else:
            print("{}/10 tests pass.".format(i + 1))


if __name__ == '__main__':

    fib1 = lambda x: x*x if x < 2 else fib1(x-1) + fib1(x-2)

    print("FIB1 TESTS")

    if len(sys.argv) != 3:
        print("Incorrect usage: no benchmarks run.")
    elif sys.argv[1] == "bench":