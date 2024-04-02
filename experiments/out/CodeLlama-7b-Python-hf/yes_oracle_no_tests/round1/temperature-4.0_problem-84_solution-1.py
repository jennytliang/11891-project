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
    # 1. Create a variable s to store the sum of digits.
    s = 0
    # 2. Convert N to a string.
    N_string = str(N)
    # 3. Iterate over the string of N.
    for i in N_string:
        # 4. Convert the string of N to an integer.
        i = int(i)
        # 5. Add the digit to the sum.
        s += i
    # 6. Convert the sum to binary.
    s = bin(s)
    # 7. Remove the "0b" from the binary.
    s = s[2:]
    # 8. Return the sum in binary.
    return s
