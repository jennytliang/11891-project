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
    
	Do not include these tokens in the code: else :
	"""

    if n > m:
         return -1
    
    total = 0
    for i in range(n, m+1):
        total += i
    
    average = total / (m-n+1)
    
    if average < 0:
        return -1
    elif average < 1:
        return "0b0"
    elif average > 1:
        return "0b1"
    else:
        return "0b1"


def test_rounded_avg():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
    assert rounded_avg(12, 15) == "0b1110"
    assert rounded_avg(10, 12) == "0b1110"
    assert rounded_avg(12, 10) == "0b1110"
    assert rounded_avg(10, 10) == "0b11"
    assert rounded_avg(10, 10) == "0b11"
    assert rounded_avg(20, 20) == "0b1"
    assert rounded_avg(1, 1) == "0b1"
    assert rounded_avg(15, 15) == "0b1"
    assert rounded_avg(16, 16) == "0b10"
    assert rounded_avg(17, 17) == "0b10"
    assert rounded_avg(18, 18) == "0b10"
    assert rounded_avg(19, 19) == "0b10"
    assert rounded_avg(20, 20) == "0b1"
    assert rounded_avg(21, 21