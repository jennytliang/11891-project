def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    pass # replace this pass with code

print(
    "sum_to_n(5) returned {0}, but the answer is 15.\n"
    "sum_to_n(10) returned {1}, but the answer is 55.\n"
    "sum_to_n(30) returned {2}, but the answer is 465.\n"
    "sum_to_n(100) returned {3}, but the answer is 5050.\n"

    "sum_to_n's signature is sum_to_n(int) with\n"
    "sum_to_n has an infinite recursion space for n. Use it.".format(
        *[sum_to_n(k) for k in (5, 10, 30, 100)]
    )
)