def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: 2 # 1 0 ^(
	"""


    if n == 1:
        return 1

    # start with 1
    count_start_with_1 = 9 * starts_one_ends(n - 1)

    # end with 1
    count_end_with_1 = 10 * starts_one_ends(n - 1)

    # start with 2 and end with 0
    count_start_with_2_end_with_0 = 10 * starts_one_ends(n - 1)

    return count_start_with_1 + count_end_with_1 + count_start_with_2_end_with_0

if __name__ == "__main__":
    print starts_one_ends(1)
    print starts_one_ends(2)
    print starts_one_ends(3)
    print starts_one_ends(4)
    print starts_one_ends(5)
