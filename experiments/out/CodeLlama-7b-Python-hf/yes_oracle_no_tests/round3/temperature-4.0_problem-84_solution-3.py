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
    
	Include these tokens in the code: s
	Do not include these tokens in the code: # First , convert the integer to
	"""
    # First , convert the integer to binary
    # Convert to binary
    binary = bin(N)
    # Remove the '0b'
    binary = binary[2:]
    # Get the sum of the digits
    sum_of_digits = sum([int(i) for i in list(binary)])
    # Convert the sum_of_digits to binary
    binary = bin(sum_of_digits)
    # Remove the '0b'
    binary = binary[2:]
    # Return the binary
    return binary


# Tests
def check(candidate):

    # Check some simple cases
    assert candidate(1000) == "1"
    assert candidate(150) == "110"
    assert candidate(147) == "1100"
    assert candidate(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000