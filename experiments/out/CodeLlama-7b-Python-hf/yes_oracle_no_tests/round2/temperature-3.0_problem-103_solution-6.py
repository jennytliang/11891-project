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
    
	Do not include these tokens in the code: # Your code here
	"""
    # Check if n is greater than m.
    if n > m:
        return -1
    # Calculate the difference between n and m.
    difference = m - n
    # Calculate the average.
    average = difference / 2 + n
    # Round the average.
    rounded_average = round(average)
    # Convert the average to binary.
    binary_average = bin(rounded_average)
    return binary_average

print(rounded_avg(1, 5)) # "0b11"
print(rounded_avg(7, 5)) # -1
print(rounded_avg(10, 20)) # "0b1111"
print(rounded_avg(20, 33)) # "0b11010"
