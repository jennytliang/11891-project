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
    def get_bin(N):
        """
        Given a positive integer N, return the sum of its digits in binary.
        """
        # Your code here
        bin_num = ""
        while N > 0:
            N, r = divmod(N, 2)
            bin_num = str(r) + bin_num
        return bin_num

    s = sum(int(i) for i in get_bin(N))
    return get_bin(s)
