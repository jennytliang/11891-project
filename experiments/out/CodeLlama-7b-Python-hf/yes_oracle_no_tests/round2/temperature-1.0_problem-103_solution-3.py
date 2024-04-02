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
    
	Include these tokens in the code: av g
	Do not include these tokens in the code: s = sum ( list ( range ( n ,
	"""


    if n > m:
        return -1
    else:
        sum = 0
        for i in range(n, m+1):
            sum = sum + i
        value = sum / (m - n + 1)
        value = round(value)
        value = bin(value)
        return value


    pass


def main():
    print(rounded_avg(1, 5))
    print(rounded_avg(1000, 2000))
    print(rounded_avg(5, 1))
    print(rounded_avg(1000000, 4000000))
    print(rounded_avg(7, 5))


if __name__ == '__main__':
    main()
