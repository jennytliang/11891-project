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
    s = str(bin(N))[2:]
    s = s.replace('0', '00')
    s = s.replace('1', '01')
    s = s.replace('2', '10')
    s = s.replace('3', '11')
    s = s.replace('4', '000')
    s = s.replace('5', '001')
    s = s.replace('6', '010')
    s = s.replace('7', '011')
    s = s.replace('8', '100')
    s = s.replace('9', '101')
    return s


































