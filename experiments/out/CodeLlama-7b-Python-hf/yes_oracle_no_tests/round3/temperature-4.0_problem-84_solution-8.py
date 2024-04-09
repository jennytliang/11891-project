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
    
	Include these tokens in the code: s = sum ( map ( lambda x : int
	Do not include these tokens in the code: # Write your code here
	"""
    # 1. convert N to binary
    # 2. sum the digits in binary
    # 3. convert sum to binary
    # 4. return the binary sum as a string
    # 5. return the string
    return str(bin(sum([int(i) for i in str(bin(N))[2:]])))[2:]
    
    
    
