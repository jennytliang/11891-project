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
    # START UNIT TEST
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 22
    assert fib4(9) == 34
    assert fib4(10) == 50
    assert fib4(11) == 74
    assert fib4(12) == 110
    assert fib4(13) == 164
    assert fib4(14) == 234
    assert fib4(15) == 324
    assert fib4(16) == 434
    assert fib4(17) == 584
    assert fib4(18) == 770
    assert fib4(19) == 974
    assert fib4(20) == 1202
    assert fib4(21) == 1458
    assert fib4(22) == 1750
    assert fib4(23) == 2064
    assert fib4(24) == 2422
    assert fib4(25) == 2748
    assert fib4(26) == 3090
    assert fib4(27) == 3454
    assert fib4(28) == 3838
    assert fib4(29) == 4242
    assert fib4(30) == 4654
    assert fib4(31) == 5084
    assert fib4(32) == 5534
    assert fib4(33) == 5994
    assert fib4(34) == 6470
    assert fib4(35) == 6962
