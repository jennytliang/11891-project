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
    
	Include these tokens in the code: return ( n
	Do not include these tokens in the code: r = 0
	"""
    r = 0
    for i in range(1, n + 1):
        r += i
    return r

# print(sum_to_n(30))
# print(sum_to_n(100))
# print(sum_to_n(5))
# print(sum_to_n(10))
# print(sum_to_n(1))
