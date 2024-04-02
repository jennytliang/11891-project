def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Set up variables
    start_ones = 0
    end_ones = 0
    
    # Calculate the number of numbers that start with 1
    for i in range(10):
        if i == 1:
            continue
        start_ones += 10 ** (n - 1) * i
    
    # Calculate the number of numbers that end with 1
    end_ones = 10 ** n - 1
    
    # Return the total
    return start_ones + end_ones

if __name__ == "__main__":
    print(starts_one_ends(2))
    print(starts_one_ends(3))
    print(starts_one_ends(4))
    print(starts_one_ends(5))
