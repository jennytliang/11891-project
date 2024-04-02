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
    # Take input and convert to binary
    N = bin(N)
    # Take the sum of the digits
    s = sum(int(x) for x in N[2:])
    # Convert the sum to binary
    s = bin(s)
    # Return the binary sum
    return s[2:]


print(solve(19))
print(solve(1000))
print(solve(150))
print(solve(147))
