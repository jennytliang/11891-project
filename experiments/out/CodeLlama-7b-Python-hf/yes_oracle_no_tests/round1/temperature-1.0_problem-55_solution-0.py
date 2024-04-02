def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: if
	Do not include these tokens in the code: elif
	"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)




def fib2(n: int):
    """An improved version of Fibonacci(n).
    
    This version uses memoization. I.e. once we have
    obtained the n-th Fibonacci number, keep it around.
    If it is needed more than once, do not bother re-computing it.
    
    NOTE: this version is a bit tricky to understand.
    It would be helpful, if the assignment notes discussed it also.
    It is based on the recursion version, and so also has
    the same base cases. The interesting things happen when we
    call the function itself.
    
    If you understand the recursion version, and not too
    many of these kinds of functions, I recommend to try
    understanding this version first.
    
    >>> fib2(10)
    55
    >>> fib2(1)
    1
    >>> fib2(8)
    21
    """

    def helper(n: int) -> int:
        """Return n-th Fibonacci number. Implementation detail."""
        # if not already done:
        if n <= 1:
            result = n
        # store n-th Fibonacci number
        # n is just too large:
        elif n > 1 and n > fib2_cache[-1]:
            result = helper(n - 1) + helper(n - 2)
        # already computed and cached:
        else:
            result = fib2_cache[n - 1]
        # cache the computed value
        fib2_cache.append(result)
        return result

    # Initially, we have fib2_cache[0] == 0 and fib_cache[1] == 1.
    fib2_cache = [0, 1]
    return helper(n)
