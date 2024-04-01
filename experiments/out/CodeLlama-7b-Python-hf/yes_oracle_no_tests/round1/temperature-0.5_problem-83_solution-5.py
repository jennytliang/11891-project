def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code:  count =  0
	"""

    # your code here
    count = 0
    for i in range(1, n):
        # 10^(n-1) - 1 + 10^(n-1) + 10^(n-1) - 1 + ... + 10^(n-1) + 1
        count += (10 ** (n - 1)) * 2
        # 10^(n-1) + 10^(n-1) + 10^(n-1) + ... + 10^(n-1) + 1
        count += (10 ** (n - 1))
        # 1 + 1 + 1 + ... + 1 + 1
        count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(starts_one_ends(3))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert starts_one_ends(3) == 144
    assert starts_one_ends(4) == 1440
    assert starts_one_ends(5) == 14400
    print("Coding complete? Click 'Check' to earn cool rewards!")
