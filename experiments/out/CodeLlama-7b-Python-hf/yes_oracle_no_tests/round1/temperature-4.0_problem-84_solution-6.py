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
    s = str(bin(N))[2:]
    s = s.replace("0", "1")
    return s


def test_function():
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"
    assert solve(32) == "100000"
    assert solve(1234) == "1110010"
    assert solve(47) == "11001"
    assert solve(10000) == "1000000000000"
    assert solve(123456789) == "11110000010110100101000001"


if __name__ == '__main__':
    test_function()
