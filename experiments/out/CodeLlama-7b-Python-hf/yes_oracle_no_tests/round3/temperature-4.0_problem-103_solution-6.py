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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # If
	"""
    
    pass


def test_cases():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
    assert rounded_avg(1, 1) == "0b1"
    assert rounded_avg(1, 2) == "0b10"
    assert rounded_avg(1, 3) == "0b11"
    assert rounded_avg(2, 3) == "0b10"
    assert rounded_avg(2, 4) == "0b11"
    assert rounded_avg(2, 5) == "0b100"
    assert rounded_avg(2, 6) == "0b101"
    assert rounded_avg(2, 7) == "0b110"
    assert rounded_avg(2, 8) == "0b111"
    assert rounded_avg(2, 9) == "0b1000"
    assert rounded_avg(2, 10) == "0b1001"
    assert rounded_avg(2, 11) == "0b1010"
    assert rounded_avg(2, 12) == "0b1011"
    assert rounded_avg(2, 13) == "0b1100"
    assert rounded_avg(2, 14) == "0b1101"
    assert rounded_avg(2, 15) == "0b1110"
    assert rounded_avg(2, 16) == "0b1111"
    assert rounded_avg(16, 15) == "0b1111"
    assert rounded_avg(16, 1