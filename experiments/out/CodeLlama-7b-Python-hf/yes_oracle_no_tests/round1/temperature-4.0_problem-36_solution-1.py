def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: num s = [ n // 1
	"""
    # Your code here
    return sum([1 for num in range(n) if num % 11 == 0 or num % 13 == 0 and num % 7 == 0])

if __name__ == "__main__":
    import doctest
    doctest.testmod()