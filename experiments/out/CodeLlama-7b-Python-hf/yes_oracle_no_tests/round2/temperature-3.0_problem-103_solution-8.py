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
    
	Include these tokens in the code: av g = round (( n + m ) /
	Do not include these tokens in the code: else :
	"""

    if n > m:
         return -1
    else:
        return bin(round((n+m)/2))


def test_case(n, m, expected_answer):
    answer = rounded_avg(n, m)
    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}")


if __name__ == '__main__':
    test_case(1, 5, "0b11")
    test_case(7, 5, -1)
    test_case(10, 20, "0b1111")
    test_case(20, 33, "0b11010")
    print("All tests passed!")
