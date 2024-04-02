def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: result = 0 for
	"""
    result = 0
    # Add your code here
    for i in range(1,10**(n-1)+1):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            result += 1
    return result

print(starts_one_ends(2))
