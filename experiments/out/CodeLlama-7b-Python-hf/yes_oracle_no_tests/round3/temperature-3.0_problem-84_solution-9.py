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
	Do not include these tokens in the code: # 1 . split the string
	"""
    # ============== YOUR CODE HERE ==============
    return bin(sum(int(i) for i in str(N)))[2:]
    # ============================================


if __name__ == '__main__':
    print("Example:")
    print(solve(1234))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert solve(1234) == "11101"
    assert solve(42) == "1010"
    assert solve(7) == "111"
    print("Coding complete? Click 'Check' to earn cool rewards!")
