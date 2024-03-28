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
    """
    # your code here
    return bin(N)[2:].replace('0','')

if __name__ == '__main__':
    print("Example:")
    print(solve(1000))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"
    print("Coding complete? Click 'Check' to earn cool rewards!")

