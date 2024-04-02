def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r
	"""


    foobar = []
    for number in range(n-1,2,-1):
        if n % number ==0:
            foobar.append(number)
    return max(foobar)

print(largest_divisor(24))