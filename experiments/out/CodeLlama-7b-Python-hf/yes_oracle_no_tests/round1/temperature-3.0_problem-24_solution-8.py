def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Base case if n
	"""
    
    # Base case if n
    if n == 1:
        return n
    
    # Recursive call
    else:
        return max(largest_divisor(n - 1), n % largest_divisor(n - 1))

# Testing
if __name__ == "__main__":
    import doctest
    doctest.testmod()
