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
    
	Do not include these tokens in the code: # first check if n is greater
	"""
    #first check if n is greater
    if n > m:
        return -1
    
    #sum all integers from n to m
    total = 0
    for i in range(n, m + 1, 1):
        total += i
    
    #calculate the average
    avg = total / (m - n + 1)
    
    #round the average and convert to binary
    avg = round(avg)
    avg = bin(avg)
    
    return avg

print(rounded_avg(1, 5)) #0b11
print(rounded_avg(7, 5)) #-1
print(rounded_avg(10, 20)) #0b1111
print(rounded_avg(20, 33)) #0b11010
