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
	Do not include these tokens in the code: binary
	"""
    # 1. Take input
    # 2. Convert to binary string
    # 3. Sum digits
    # 4. Convert to string
    # 5. Return the string
    return str(sum(int(i) for i in bin(N)[2:]))


### DO NOT TOUCH CODE BELOW THIS LINE ###
if __name__ == '__main__':
    print(solve(int(input())))
