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
	Do not include these tokens in the code: return str (
	"""
    
    # Write your code here
    s = 0
    for i in range(0,N):
        s += N % 10
        N = N//10
    return bin(s)
    
    # def convert_to_binary(N):
    #     return bin(N)
    
    # def solve(N):
    #     return convert_to_binary(N)
    
    # print(solve(1000))
    # print(solve(150))
    # print(solve(147))

    # def convert_to_binary(N):
    #     return bin(N)
    
    # def solve(N):
    #     return convert_to_binary(N)
    
    # print(solve(1000))
    # print(solve(150))
    # print(solve(147))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    