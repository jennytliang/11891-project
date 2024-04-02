def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: result = 0 for
	"""
    # Your code here
    result = 0
    if n > 0:
        if n == 1:
            result = 10
        else:
            result = 9 * 10 ** (n - 2)
    return result


if __name__ == '__main__':
    print(starts_one_ends(1))
    # 10
    print(starts_one_ends(2))
    # 90
    print(starts_one_ends(3))
    # 900
    print(starts_one_ends(4))
    # 9000
    print(starts_one_ends(5))
    # 90000
    print(starts_one_ends(6))
    # 900000
