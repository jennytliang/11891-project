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
    # 1. Convert N to binary
    # 2. convert each digit to int
    # 3. sum the digits
    # 4. convert the sum back to binary
    # 5. return the binary string
    # 6. convert the binary string back to integer
    # 7. return the integer
    return bin(sum(map(int, bin(N)[2:])))[2:]


def test_function():
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'
    assert solve(100000000) == '100000000'
    assert solve(1000000000) == '1000000001'
    assert solve(10000000000) == '10000000010'
