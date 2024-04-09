def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # Your code here
	"""
    return 10 ** (n - 1)


def main():
    n = 3
    print("n:", n)
    print("Count of the numbers of n-digit positive integers that start or end with 1:")
    print(starts_one_ends(n))


if __name__ == "__main__":
    main()
