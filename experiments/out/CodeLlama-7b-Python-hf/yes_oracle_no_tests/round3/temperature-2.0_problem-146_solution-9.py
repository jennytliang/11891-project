def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

   # Initialize the counter
    count = 0

    # Loop through the list
    for num in nums:

        # Check if the number is greater than 10
        if num > 10:

            # Check if the first digit is odd
            if num % 10 % 2 == 1:

                # Check if the last digit is odd
                if num // 10 % 2 == 1:

                    # Increment the counter
                    count += 1

    # Return the counter
    return count
