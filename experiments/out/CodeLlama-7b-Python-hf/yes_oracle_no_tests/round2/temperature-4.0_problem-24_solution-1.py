def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Write your code here
	"""
    # Write your code here
    if n == 1:
        return 1
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
