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
    
	Do not include these tokens in the code: # s = sum ( map (
	"""
    # s = sum ( map ( lambda x: bin ( x ) [ 2: ], str ( N ) ) ) ) [ 2: ]
    # return s

    # s = sum ( map ( lambda x: bin ( x ) [ 2: ], str ( N ) ) )
    # return s

    # s = sum ( map ( lambda x: bin ( x ) [ 2: ], str ( N ) ) )
    # return s

    # s = sum ( map ( lambda x: bin ( x ) [ 2: ], str ( N ) ) )
    # return s

    s = sum ( map ( lambda x: bin ( x ) [ 2: ], str ( N ) ) )
    return s


if __name__ == '__main__':
    print("Example:")
    print(solve(1000))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'
    assert solve(123) == '11110'
    assert solve(999) == '10011'
    print("Coding complete? Click 'Check' to earn cool rewards!")
