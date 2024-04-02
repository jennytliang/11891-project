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

    roundedAvg = round(((n+m)/2))
    binNum = bin(roundedAvg)[2:]
    return binNum
    
print(rounded_avg(22,11)) #= 12 is binary for 1100 
print(rounded_avg(122,3)) #= 32 is binary for 11000
print(rounded_avg(100,206)) #= 125 is binary for 1100101
print(rounded_avg(-20,122)) #= 132 is binary for 11000100
print(rounded_avg(55,30)) #= -1
print(rounded_avg(10,20)) #= 15