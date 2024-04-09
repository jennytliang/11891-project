def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # W R ITE Y OUR CO
	"""
    # Your code here
    count = 0
    for i in range(10**(n-1), 10**n):
        if (i % 10 == 1 or i // 10**(n-1) == 1):
            count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(starts_one_ends(1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert starts_one_ends(1) == 8
    assert starts_one_ends(2) == 49
    print("Coding complete? Click 'Check' to earn cool rewards!")
