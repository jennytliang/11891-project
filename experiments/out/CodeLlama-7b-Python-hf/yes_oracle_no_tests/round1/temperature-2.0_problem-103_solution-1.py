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
    
	Include these tokens in the code: if n > m : return - 1
	"""
    #print(n,m)
    if n > m:
        return -1
    elif n == m:
        return n
    else:
        average = round((n+m)/2)
        return bin(average)
    
def main():
    print(rounded_avg(1, 5)) # => "0b11"
    print(rounded_avg(7, 5)) # => -1
    print(rounded_avg(10, 20)) # => "0b1111"
    print(rounded_avg(20, 33)) # => "0b11010"
    print(rounded_avg(1, 1)) # => "0b1"
    print(rounded_avg(10, 10)) # => "0b1010"
    print(rounded_avg(10, 11)) # => -1
    print(rounded_avg(10, 9)) # => -1
    print(rounded_avg(10, 1)) # => -1
    print(rounded_avg(1, 10)) # => "0b1010"
    print(rounded_avg(1, 100)) # => "0b1100100"
    print(rounded_avg(100, 100)) # => "0b1100100"
    print(rounded_avg(100, 1)) # => -1
    print(rounded_avg(100, 99)) # => -1
    print(rounded_avg(99, 100)) # => -1
    print(rounded_avg(99, 101)) # => -1
    print(rounded_avg(100, 101)) # => -1
    print(rounded_avg(101, 100)) # => -1
    print(rounded_avg(1