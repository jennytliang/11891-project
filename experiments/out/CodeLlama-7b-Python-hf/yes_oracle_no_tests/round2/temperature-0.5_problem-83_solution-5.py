def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    return 10 ** (n - 1)


if __name__ == "__main__":
    print(starts_one_ends(1))
    print(starts_one_ends(2))
    print(starts_one_ends(3))
