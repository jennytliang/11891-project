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
	Do not include these tokens in the code: return bin (
	"""
    
    n = N
    s= 0
    while n > 0:
        
        remainder = n % 2
        s += remainder
        
        n //= 2
        
    print(bin(s))
    return bin(s)

# test sol1
N = 123
output = solve(N)
print("sol1: ")
print(output)
output
# test sol2
print("\nsol2: ")
solve2(N)