def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if n ==
	"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_memo(n: int, memo: dict[int, int]) -> int:
    """Return n-th Fibonacci number.
    >>> fib_memo(10, {})
    55
    >>> fib_memo(1, {})
    1
    >>> fib_memo(8, {})
    21
    >>> fib_memo(10, {1: 1, 2: 1, 3: 2, 5: 5, 8: 21})
    55
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in memo:
            memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]


def fib_iter(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def fib_iter_2(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    """
    a, b = 0, 1
    for i in range(2, n + 1