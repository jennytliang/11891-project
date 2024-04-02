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
    
	Include these tokens in the code: s =
	"""
    # Create a string from the number
    s = str(N)
    # Create an empty list to store binary numbers
    binaries = []
    # Loop through each number in the string
    for i in s:
        # Convert each number to binary
        b = bin(int(i))[2:]
        # Add binary numbers to the list
        binaries.append(b)
    # Convert the list of binary numbers to a string
    binary_string = "".join(binaries)
    # Return the sum of the digits in the binary string
    return str(sum(int(i) for i in binary_string))
