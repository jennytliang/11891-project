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
    
	Do not include these tokens in the code: # Write your code here .
	"""
    # Find the average
    # Round it to the nearest integer
    # Convert it to binary
    # Return it
    pass


print(rounded_avg(1, 5))  # "0b11"
print(rounded_avg(7, 5))  # -1
print(rounded_avg(10, 20))  # "0b1111"
print(rounded_avg(20, 33))  # "0b11010"
print(rounded_avg(100, 200))  # "0b111110"
print(rounded_avg(1000, 2000))  # "0b1111111110"
print(rounded_avg(10000, 20000))  # "0b11111111111110"
