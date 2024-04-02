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
    
	Include these tokens in the code: s =
	"""
    
    # 1) convert the integer to binary
    N_bin = bin(N)[2:]
    
    # 2) convert the binary to a list of integers
    N_bin_list = [int(i) for i in N_bin]
    
    # 3) sum the list of integers
    N_bin_sum = sum(N_bin_list)
    
    # 4) convert the sum to binary
    N_bin_sum_bin = bin(N_bin_sum)[2:]
    
    # 5) return the binary number as a string
    return str(N_bin_sum_bin)
    