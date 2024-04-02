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
	"""
    # 1. Convert to binary
    # 2. Convert to list of ints
    # 3. sum that list
    # 4. Convert to binary
    return bin(sum(map(lambda x: int(x), bin(N)[2:])))[2:]


if __name__ == '__main__':
    print(solve(1000))
