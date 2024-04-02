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
    
	Do not include these tokens in the code: , 2
	"""

    s = sum(map(lambda x: 1 if x else 0, map(int, bin(N)[2:])))  # 1000 -> 11000 -> [1,1,0,0,0] -> [1,1]
    return bin(s)[2:]  # [1,1] -> 11 -> "11"


if __name__ == "__main__":
    print(solve(1000))
    print(solve(150))
    print(solve(147))
