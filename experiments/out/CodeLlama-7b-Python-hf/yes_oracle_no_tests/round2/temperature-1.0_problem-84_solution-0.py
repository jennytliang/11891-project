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
    # input validatation
    if N <= 0 and N > 10 ** 4:
        raise ValueError

    bin_str = bin(N)[2:]    # convert to bin(N) and discard the heading '0b' or '0B'
    bin_n = 0
    for digit in bin_str:
        bin_n += int(digit)    # add up to get the total sum of digits in binary
    return bin(bin_n)[2:]    # returns binary number str


if __name__ == '__main__':
    N = int(input())
    print(solve(N))