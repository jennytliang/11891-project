def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return 1
    elif n == 2:
        return 8
    elif n == 3:
        return 16
    else:
        return 16**(n-1) + 8*(16**(n-2))


if __name__ == "__main__":
    print(starts_one_ends(4))
