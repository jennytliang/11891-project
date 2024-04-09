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
	Do not include these tokens in the code: return str (
	"""
    s = sum(int(i) for i in bin(N)[2:])
    return bin(s)[2:]


def test_solution1():
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'


def test_solution2():
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'


def test_solution3():
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'


def test_solution4():
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'
