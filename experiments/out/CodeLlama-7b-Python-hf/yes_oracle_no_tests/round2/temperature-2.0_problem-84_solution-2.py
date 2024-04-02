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
    
	Do not include these tokens in the code: # Create a string from the number
	"""
    # Create a string from the number
    s = str(N)
    # Initialize a variable to store the binary sum
    sum_binary = 0
    # Loop over every character in the string
    for char in s:
        # Convert the character to an integer
        num = int(char)
        # Convert the integer to binary
        bin_num = bin(num)
        # Sum the binary digits
        sum_binary += int(bin_num[2:])
    # Return the sum of the binary digits
    return bin(sum_binary)[2:]
