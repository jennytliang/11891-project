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
	"""

    if n > m:
         return -1

    avg = round((n + m) / 2)

    # Convert the number to binary
    # Set the number of digits to 4
    # I didn't know how to do this part
    # so I used a loop to do it

    # Set the number of digits to 4
    digits = 4

    # Set up the binary number to 0
    binary_num = 0

    # Set up the counter to 0
    counter = 0

    # Set up the power of 2
    power = 1

    # Loop through the digits
    while counter < digits:

        # Add the value of the power to the binary number
        binary_num += (avg * power)

        # Increase the power by 2
        power *= 2

        # Increase the counter by 1
        counter += 1

    # Convert the binary number to a string
    binary_num = str(binary_num)

    # Return the binary number
    return binary_num


print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))
