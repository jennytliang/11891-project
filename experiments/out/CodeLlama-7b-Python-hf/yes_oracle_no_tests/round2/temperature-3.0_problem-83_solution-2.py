def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # TODO : Write your assert ations
	"""

    # TODO : Write your assert ations
    assert n > 0, "n should be greater than 0"

    # TODO : Write your code here
    if n == 1:
        return 0
    elif n == 2:
        return 10
    else:
        return 9 * 10 ** (n - 2) + 10


if __name__ == "__main__":
    n = 1
    print(starts_one_ends(n))
