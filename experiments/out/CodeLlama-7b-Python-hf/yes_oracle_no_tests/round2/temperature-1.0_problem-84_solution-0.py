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
    
	Include these tokens in the code: str
	Do not include these tokens in the code: bin
	"""

    s = sum(map(lambda x: in_binary(x), list(str(N))))
    return str(s)


def in_binary(x):
    return int(x, 2)


print(solve(6))
