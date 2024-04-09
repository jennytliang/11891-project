def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    
	Include these tokens in the code: : return 0 if
	Do not include these tokens in the code: or
	"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# This provided code fills in the values for the variables a0
# through a4. You can run it as 
# fill_in_the_blanks(a0, a1, a2, a3, a4)
# but the point is that you don't need to do that inside
# of the function.

def fill_in_the_blanks(a0, a1, a2, a3, a4):
    a0 = 0
    a1 = 1
    a2 = 1
    a3 = fib(3)
    a4 = fib(8)


if __name__ == "__main__":
    fill_in_the_blanks(a0, a1, a2, a3, a4)
    print(a0, a1, a2, a3, a4)
