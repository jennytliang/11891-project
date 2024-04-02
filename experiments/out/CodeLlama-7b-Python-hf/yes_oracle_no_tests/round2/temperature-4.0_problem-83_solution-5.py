def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: else :
	"""

    if n == 1:
        return 2

    count = 0
    for i in range(1, 10):
        count += starts_one_ends(n - 1)

    return count


if __name__ == "__main__":
    print(starts_one_ends(5))
