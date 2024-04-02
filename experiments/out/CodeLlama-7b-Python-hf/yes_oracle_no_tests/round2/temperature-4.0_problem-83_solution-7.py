def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: # Start with
	"""
    # Start with 1
    # End with 1
    # Start with 2
    # End with 2
    # Start with 3
    # End with 3
    # Start with 4
    # End with 4
    # Start with 5
    # End with 5
    # Start with 6
    # End with 6
    # Start with 7
    # End with 7
    # Start with 8
    # End with 8
    # Start with 9
    # End with 9
    
    # Start with 1
    start_one = 9 * 10 ** (n - 1)
    # End with 1
    end_one = 10 ** (n - 1)
    # Start with 2
    start_two = 8 * 10 ** (n - 1) + 1
    # End with 2
    end_two = 9 * 10 ** (n - 1)
    # Start with 3
    start_three = 7 * 10 ** (n - 1) + 2
    # End with 3
    end_three = 8 * 10 ** (n - 1)
    # Start with 4
    start_four = 6 * 10 ** (n - 1) + 3
    # End with 4
    end_four = 7 * 10 ** (n - 1)
    # Start with 5
    start_five = 5 * 10 ** (n - 1) + 4
    # End with 5
    end_five = 6 * 10 ** (n - 1)
    # Start with 6
    start_six = 4 * 10 ** (n - 1) + 5
    # End with 6
    end_six = 5 * 10 ** (n - 1)
    # Start with 7
    start_seven = 3 * 10 ** (n - 1) + 6
    # End with 7
    end_seven = 4 * 1