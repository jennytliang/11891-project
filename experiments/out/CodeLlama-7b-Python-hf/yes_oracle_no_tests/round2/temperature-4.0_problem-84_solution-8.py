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
    # Write your code here
    return bin(sum(int(i) for i in str(N)))[2:]


# DO NOT REMOVE THIS COMMENT
# DO NOT CHANGE THE API BELOW THIS LINE
# api.difficulty = 1
# api.preferred_result_format = 'json'
# api.parameters = 'N'
