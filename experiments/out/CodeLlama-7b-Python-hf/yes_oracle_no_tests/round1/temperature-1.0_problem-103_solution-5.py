def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
	Include these tokens in the code: round ((
	Do not include these tokens in the code: (
	"""

    if n > m:
        return -1

    return bin(round((m - n + 1) / 2))



def test_case(n, m, expected, f):
    result = f(n, m)
    if expected == result:
        print("PASSED: expected {0} but got {1}".format(expected, result))
    else:
        print("FAILED: expected {0} but got {1}".format(expected, result))


def test(f):
    test_case(1, 5, "0b11", f)
    test_case(7, 5, -1, f)
    test_case(10, 20, "0b1111", f)
    test_case(20, 33, "0b11010", f)


if __name__ == "__main__":
    test(rounded_avg)
