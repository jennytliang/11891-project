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
    
	Include these tokens in the code: return
	Do not include these tokens in the code: # Write your code here .
	"""
    # Write your code here.
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
