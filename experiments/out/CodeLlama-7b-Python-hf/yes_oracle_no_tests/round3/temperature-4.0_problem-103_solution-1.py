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
    
	Do not include these tokens in the code: # Find the average of the numbers
	"""
    avg = (n + m) // 2
    if n > m:
        return -1
    return "0b" + str(bin(avg))[2:].rjust(5, "0")


if __name__ == '__main__':
    print(rounded_avg(1, 5))
    print(rounded_avg(7, 5))
    print(rounded_avg(10, 20))
    print(rounded_avg(20, 33))
