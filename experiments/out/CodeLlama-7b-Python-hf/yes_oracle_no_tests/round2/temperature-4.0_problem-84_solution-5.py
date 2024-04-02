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
    
	Do not include these tokens in the code: assert ( N >= 0 and
	"""
    # 1. Take the integer, N and convert to binary
    # 2. Split the binary number into a list of binary digits
    # 3. Sum the digits in the list
    # 4. Convert the sum back to a binary number
    # 5. Return the binary number
    return bin(sum([int(x) for x in str(bin(N))[2:]])).replace('0b', '')


# N = 147
# print(solve(N))
