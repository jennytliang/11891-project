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
    """

    assert(N >= 0), "The input value should be 0 or more."

    return f"{bin(N).replace('0b', '')}"




# py.test
'''
def test_solve():
    assert solve(100) == '1100100', f'The solution for N=100 should return 1100100 not {solve(100)}'
    assert solve(150) == '1110100', f'The solution for N=150 should return 1110100 not {solve(150)}'
    assert solve(0) == '0', f'The solution for N=0 should return 0 not {solve(0)}'