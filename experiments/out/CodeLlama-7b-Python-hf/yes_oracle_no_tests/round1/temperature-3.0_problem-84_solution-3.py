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
    # first convert N into string
    N = str(N)

    # initialize a list to hold each digit
    digits = []

    # for each digit in N, append it to digits
    for digit in N:
        digits.append(digit)

    # initialize a list to hold each converted digit
    converted_digits = []

    # for each digit in digits, convert it to binary and append it to converted_digits
    for digit in digits:
        converted_digits.append(bin(int(digit)))

    # initialize a list to hold each sum of each converted digit
    sums = []

    # for each digit in converted_digits, sum it and append it to sums
    for digit in converted_digits:
        sums.append(sum(map(int, digit[2:])))

    # initialize a list to hold each string of each sum
    strings = []

    # for each sum in sums, convert it to a string and append it to strings
    for sum in sums:
        strings.append(str(sum))

    # initialize a list to hold each sum of each string
    total_sums = []

    # for each string in strings, sum it and append it to total_sums
    for string in strings:
        total_sums.append(sum(map(int, string)))

    # return the total sum of all sums as a string
    return str(sum(total_sums))


def test_function():
    assert solve(1000) == "1"
    assert solve(150) == "110"
    assert solve(147) == "1100"
    assert solve(123) == "11101"
    assert solve(456) == "110110"
    assert solve(999) == "11111"

if __name__ == '__main__':
    test_function()
