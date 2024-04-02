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
    
	Do not include these tokens in the code: # Take input and convert to binary
	"""
    # Take input and convert to binary
    N = bin(N)
    # Convert to string
    N = str(N)
    # Remove the '0b'
    N = N[2:]
    # Split the string into a list of individual digits
    N = N.split()
    # Convert the list of digits back to a string
    N = ''.join(N)
    # Sum the digits
    N = sum([int(i) for i in N])
    return N


# Testing
N = 147
assert solve(N) == 12
N = 150
assert solve(N) == 6
N = 1000
assert solve(N) == 1
