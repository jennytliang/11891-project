def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: <
	"""

    # count of numbers with 1 as first digit
    n1 = 10**(n-1)

    # count of numbers with 1 as last digit
    n2 = 10**(n-1)

    # count of numbers with 1 as first and last digit
    n3 = 10**(n-2)

    return n1 + n2 - 2*n3


if __name__ == '__main__':
    assert starts_one_ends(1) == 9
    assert starts_one_ends(2) == 90
    assert starts_one_ends(3) == 900
    assert starts_one_ends(4) == 9000
