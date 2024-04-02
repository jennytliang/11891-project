def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: result = 0 for
	"""
    # Initialize the count of numbers that start or end with 1
    count = 0
    # Loop from 1 to n
    for i in range(1, n + 1):
        # Add 1 to the count
        count += 2
        # If the number of digits is greater than or equal to 3
        if i >= 3:
            # Subtract 1 from the count
            count -= 1
    # Return the count of numbers that start or end with 1
    return count


# Call the starts_one_ends function
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(5))
