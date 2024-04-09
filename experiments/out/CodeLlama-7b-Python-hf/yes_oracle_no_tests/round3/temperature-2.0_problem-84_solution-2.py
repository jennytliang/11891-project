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
    
	Do not include these tokens in the code: # Create a string from the number
	"""
    # Write your code here
    binary = bin(N)[2:]
    total = 0
    for i in range(len(binary)):
        total += int(binary[i])
    return bin(total)[2:]


print(solve(1000))
print(solve(150))
print(solve(147))
