def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Initialize count of numbers starting with 1
    count_starting_with_one = 0
    # Initialize count of numbers ending with 1
    count_ending_with_one = 0

    # Initialize the range of values to check
    range_of_values = 10 ** (n - 1)

    # Count the number of numbers starting with 1
    count_starting_with_one = range_of_values - (range_of_values // 10)

    # Count the number of numbers ending with 1
    count_ending_with_one = range_of_values // 10

    # Combine the counts
    return count_starting_with_one + count_ending_with_one
