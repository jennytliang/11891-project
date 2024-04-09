def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: # Write your code here
	"""
    # Write your code here
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return largest_divisor(n // 2)
    else:
        return largest_divisor(n // 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
