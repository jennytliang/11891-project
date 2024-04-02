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
    
	Do not include these tokens in the code: # first convert N to binary
	"""
    # write your code here
    # return the sum of digits in binary
    return bin(N)[2:].replace('0', '#').replace('1', '10').replace('#', '1').count('1')


def main():
    N = 150
    print(solve(N))


if __name__ == "__main__":
    main()