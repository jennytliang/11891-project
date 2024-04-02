def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: count = 0 for
	"""
    # your code here
    count = 0
    if n == 1:
        return 0
    for i in range(1, 10**(n-1)):
        if str(i).startswith("1") or str(i).endswith("1"):
            count += 1
    return count


if __name__ == "__main__":
    print(starts_one_ends(1))
    print(starts_one_ends(2))
    print(starts_one_ends(3))
    print(starts_one_ends(4))
