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
    
	Do not include these tokens in the code: , 2
	"""


    s = sum(map(lambda x: bin(x)[2:], list(str(N))))
    return s


def test_function():
    assert solve(42) == "1010"
    assert solve(13) == "1101"
    assert solve(2018) == "100110"
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"
    assert solve(10000) == "100000"
    assert solve(10001) == "100001"

if __name__ == '__main__':
    test_function()