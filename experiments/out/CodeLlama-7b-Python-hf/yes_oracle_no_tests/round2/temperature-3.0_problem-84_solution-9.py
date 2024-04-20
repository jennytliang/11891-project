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
    
	Include these tokens in the code: s
	Do not include these tokens in the code: # 1 . split the string
	"""
    # 1. split the string
    # 2. convert each digit into binary
    # 3. sum the binary digits
    # 4. convert the sum into string
    # 5. return the string
    sum = 0
    for i in str(bin(N))[2:]:
        sum += int(i)
    return str(bin(sum))[2:]


print(solve(1000))
print(solve(150))
print(solve(147))