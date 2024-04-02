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
    #1.
    # s = str(bin(N))[2:]
    # return s
    #2.
    # return str(bin(N))[2:].replace("0","").replace("1","1")
    #3.
    # return str(bin(N))[2:].replace("0","1")
    #4.
    s = str(bin(N))[2:]
    return s.replace("0","1")
    #5.
    # return str(bin(N))[2:].replace("0","1").replace("1","1")
    #6.
    # return str(bin(N))[2:].replace("0","1").replace("1","1").replace("11","1")
    #7.
    return str(bin(N))[2:].replace("0","1").replace("1","1").replace("11","1").replace("111","1")
    #8.
    return str(bin(N))[2:].replace("0","1").replace("1","1").replace("11","1").replace("111","1").replace("1111","1")


if __name__ == '__main__':
    print(solve(147))
    print(solve(150))
    print(solve(1000))
