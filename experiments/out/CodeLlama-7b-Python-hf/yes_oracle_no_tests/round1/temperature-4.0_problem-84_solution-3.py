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
    
	Include these tokens in the code: s = sum
	Do not include these tokens in the code: def get _ bin
	"""
    # First, convert the integer to binary.
    # Then, split the binary string into a list of characters.
    # Then, convert the list of characters to integers.
    # Then, add up the integers.
    # Finally, convert the sum to a string.
    
    # Your code here
    return bin(N)[2:].replace('0','').replace('1','10')
    
    
solve(1000)