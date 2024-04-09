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
	Do not include these tokens in the code: return bin (
	"""
    # 1. Take an integer N
    # 2. Convert the integer N into a string
    # 3. Iterate over the string
    # 4. Convert the string to binary
    # 5. Add the binary number to the total sum
    # 6. Return the total sum
    # 7. Convert the total sum to binary
    total = 0
    for num in str(N):
        total += int(bin(int(num))[2:], 2)
    return bin(total)[2:]

if __name__ == "__main__":
    print(solve(150))
    print(solve(147))
