def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Do not include these tokens in the code: # your code here
	"""
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[0] + lst[1]
    if len(lst) == 3:
        return lst[0] + lst[1] + lst[2]
    if len(lst) == 4:
        return lst[0] + lst[1] + lst[2] + lst[3]

    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_digits(num):
        if num < 10:
            return num
        else:
            return num % 10 + sum_digits(num // 10)

    def largest_prime(lst):
        if len(lst) == 1:
            return lst[0]
        if len(lst) == 2:
            if is_prime(lst[0]) and is_prime(lst[1]):
                if lst[0] > lst[1]:
                    return lst[0]
                else:
                    return lst[1]
            else:
                if is_prime(lst[0]):
                    return lst[0]
                else:
                    return lst[1]
        if len(lst) == 3:
            if is_prime(lst[0]) and is_prime(lst[1]) and is_prime(lst[2]):
                if lst[0] > lst[1] and lst[0] > lst[2]:
                    return lst[0]
                elif lst[1] > lst[2]:
                    return lst[1]
                else:
                    return lst[2]
            else:
                if is_prime(lst[0]):
                    return lst[0]
                if is_prime(lst[1]):
                    return lst[