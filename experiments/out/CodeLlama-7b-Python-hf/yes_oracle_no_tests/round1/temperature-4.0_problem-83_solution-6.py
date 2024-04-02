def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Start with 10 to 10^n - 1
    start_one_ends = 0
    end_one_ends = 0
    
    # For loop to count numbers that start or end with 1
    for i in range(10 ** (n - 1), 10 ** n):
        if str(i)[:1] == '1' and str(i)[-1:] == '1':
            start_one_ends += 1
        elif str(i)[:1] == '1':
            start_one_ends += 1
        elif str(i)[-1:] == '1':
            end_one_ends += 1

    return start_one_ends + end_one_ends

print(starts_one_ends(3))
