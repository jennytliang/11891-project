def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r n age
	"""


    foobar = [int(n/i) for i in range(1,n+1)]
    return max(foobar)