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
	"""

    # Write your code here
    # s = sum ( map ( lambda x : int ( bin ( x ) [ 2: ] , N ) , range ( 1 , N + 1 ) ) )
    # return bin ( s ) [ 2: ]
    return str( sum( map( lambda x : int ( bin ( x ) [ 2: ] , range ( 1 , N + 1 ) ) ) ) )


if __name__ == '__main__':
    print("Example:")
    print(solve(1000))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert solve(1000) == "11111111111111111111111111111111"
    assert solve(150) == "110011001100110011001100110011001100"
    assert solve(147) == "110011001100110011001100110011001100"
    print("Coding complete? Click 'Check' to earn cool rewards!")
