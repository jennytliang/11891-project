def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # Your code here
	"""

    # Initialize a counter
    count = 0

    # Check for numbers that start with 1
    for i in range(10**(n-1), 10**n):
        if str(i).startswith('1'):
            count += 1

    # Check for numbers that end with 1
    for i in range(10**(n-1), 10**n):
        if str(i)[-1] == '1':
            count += 1

    return count

print(starts_one_ends(3)) # 10
print(starts_one_ends(6)) # 121