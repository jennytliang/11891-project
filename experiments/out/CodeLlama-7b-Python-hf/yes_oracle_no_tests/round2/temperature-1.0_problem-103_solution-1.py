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
    
    round_down = (n + m) // 2
    round_up = (n + m - 1) // 2

    return bin(round_down)[2:] + "1" if round_down == round_up else bin(round_up)[2:] + "0"


if __name__ == '__main__':
    print("Example:")
    print(rounded_avg(1, 5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"
    print("Coding complete? Click 'Check' to earn cool rewards!")
