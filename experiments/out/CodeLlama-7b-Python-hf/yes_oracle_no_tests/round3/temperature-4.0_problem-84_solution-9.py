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
    
	Do not include these tokens in the code: #
	"""
    # The sum of digits in binary
    bin_sum = 0
    # Convert N to binary
    bin_N = bin(N)[2:]
    # Iterate through each digit of bin_N
    for i in range(len(bin_N)):
        # Add the digit to bin_sum
        bin_sum += int(bin_N[i])
    # Convert bin_sum to binary
    return bin(bin_sum)[2:]


# print(solve(1000))
# print(solve(150))
print(solve(147))


