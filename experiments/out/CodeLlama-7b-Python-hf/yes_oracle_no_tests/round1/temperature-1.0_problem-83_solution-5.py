def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: count = 0 for
	"""

	# First thing to check is if n is valid
	if not n or n < 0:
		return "Input Error"

	# Next thing to check is if we have already had a one in this loop
	# We will need the value to be accessible outside the loops...
	hasone = False

	# We also need to keep track of the number of iterations that happen
	# We will need the value to be accessible outside the loops...
	iterations = 0

	# Create variable that will be accessible throughout the function
	n_count = 0

	# Create variables that we can increment to keep track of number start and end the with "1"
	s_one_count = 0
	e_one_count = 0

	# Create the loop to begin iterations
	for i in range(0, 2**n):

		# For every iteration reset the value hasone to false
		hasone = False

		# If we have already had a 1 in this loop, we will just have to skip it
		if not hasone:

			# Create an empty string
			bin_string = ''

			# Create a variable to keep the i to be reversed later
			backward_i = i

			# Flip i
			for l in range(0, n):

				# Add the number to the string
				bin_string = str(backward_i % 2) + bin_string

				# Go to the next digit
				backward_i = backward_i // 2
			rev_bin_string = bin_string[::-1]
			
				# For each iteration we go through 2**n (or n times)
				# We reset the i every time we go through a digit
				i = 0

				# We use the binary string starting with a one or ending with a one
				for g in rev_bin_string:

					# The next