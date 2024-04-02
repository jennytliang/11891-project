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
	Do not include these tokens in the code: # First , convert the integer to
	"""
    # First , convert the integer to binary
    bin_num = bin(N)
    # Then , convert the binary number to a list of integers
    bin_list = [int(i) for i in bin_num[2:]]
    # Finally , convert the list of integers to a string of binary numbers
    bin_str = ''.join(str(i) for i in bin_list)
    # the sum of digits in binary
    sum_bin = 0
    for i in bin_str:
        sum_bin += int(i)
    return str(sum_bin)


# print(solve(1000))