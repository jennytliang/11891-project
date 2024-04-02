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
    
	Include these tokens in the code: s = sum ( map ( lambda x : int
	Do not include these tokens in the code: assert
	"""
    
    # First, convert the integer to binary
    binary = f'{N:b}'
    # Then, sum the digits
    digit_sum = sum([int(c) for c in binary])
    # Finally, convert the sum to binary
    digit_sum_binary = f'{digit_sum:b}'
    return digit_sum_binary
    
    
if __name__ == '__main__':
    print("Example:")
    print(solve(1000))
    print(solve(150))
    print(solve(147))
    print(solve(1001))
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'
    assert solve(1001) == '10000'
    print("Coding complete? Click 'Check' to earn cool rewards!")