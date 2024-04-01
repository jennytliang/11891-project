def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: # Your code here
	"""

	# Start with a list of all the possible numbers with n digits
	numbers = [i for i in range(10**(n-1), 10**n)]
	
	# Split the list of numbers into those that start with 1 and those that end with 1
	starting = [i for i in numbers if i % 10 == 1]
	ending = [i for i in numbers if i // 10**(n - 1) == 1]
	
	# Return the length of the lists
	return len(starting) + len(ending)

print(starts_one_ends(1))