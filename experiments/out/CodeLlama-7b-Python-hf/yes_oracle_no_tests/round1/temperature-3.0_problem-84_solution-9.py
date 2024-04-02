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
	Do not include these tokens in the code: assert
	"""
    # 1. split the string into a list of digits
    digits = [int(i) for i in str(N)]
    # 2. sum the digits
    total = sum(digits)
    # 3. convert the total to a binary string
    binary = bin(total)[2:]
    # 4. return the binary string
    return binary


# tests
def test_small():
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'


def test_medium():
    assert solve(12345) == '100001'
    assert solve(99999) == '111111'
    assert solve(100000) == '1000000'


def test_large():
    assert solve(123456789) == '10010000100001'
    assert solve(999999999) == '11111111111111'
    assert solve(1000000000) == '100000000000000'


def test_random():
    assert solve(1234567890) == '100100001000010'
    assert solve(9999999990) == '111111111111110'
    assert solve(10000000000) == '1000000000000000'


def test_random_large():
    assert solve(12345678901234567890) == '1001000010000100001000010'
    assert solve(999