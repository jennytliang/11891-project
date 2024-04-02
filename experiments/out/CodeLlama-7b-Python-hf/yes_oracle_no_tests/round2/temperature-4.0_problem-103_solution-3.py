def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
	Include these tokens in the code: av g = round (( n + m ) /
	Do not include these tokens in the code: else :
	"""

    
    if n > m:
    # If n is greater than m, return -1.
        return -1
    else:
    # Round the answer to the nearest integer and convert that to binary.
        g = round((n + m) / 2)
        return bin(g)

    # Store the result in a variable called answer.
    # If n is greater than m, return -1.
    
    # Hint: You can use the bin() function to convert an integer to binary.
    # If n is less than m, then round the average of n and m to the nearest integer.
    # Convert that integer to binary.
    
    # Store the result in a variable called answer.
    # If n is greater than m, return -1.
    
    # Hint: You can use the bin() function to convert an integer to binary.
    # If n is less than m, then round the average of n and m to the nearest integer.
    # Convert that integer to binary.


print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))
