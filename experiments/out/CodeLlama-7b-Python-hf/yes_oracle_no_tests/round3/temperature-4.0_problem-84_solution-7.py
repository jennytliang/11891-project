def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    
	Include these tokens in the code: s
	Do not include these tokens in the code: # Take input and convert to binary
	"""
    
    # Take input and convert to binary
    binary = bin(N)
    binary = binary[2:]

    # Convert binary number to sum of digits
    sum_of_digits = 0
    for i in binary:
        sum_of_digits += int(i)

    # Convert sum of digits to binary
    binary = bin(sum_of_digits)
    binary = binary[2:]

    # Return binary
    return binary


# Testing
print(solve(1000))
print(solve(150))
print(solve(147))
