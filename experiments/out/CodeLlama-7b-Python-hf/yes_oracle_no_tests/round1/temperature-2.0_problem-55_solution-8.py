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
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib_fast(n: int):
    """Return n-th Fibonacci number.
    >>> fib_fast(10)
    55
    >>> fib_fast(1)
    1
    >>> fib_fast(8)
    21
    >>> fib_fast(20)
    6765
    >>> fib_fast(30)
    832040
    """
    if n < 2:
        return n
    else:
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])
        return result[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
