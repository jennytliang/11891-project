def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    
	Include these tokens in the code: if x > y : return - 1
	"""
    if x > y:
        return -1
    else:
        for i in range(x, y+1):
            if i % 2 == 0:
                return i


#print(choose_num(12, 15))
#print(choose_num(13, 12))


# 2.

"""
Write a function that takes a positive integer x and returns the sum of the
digits of x. If a number has more than 9 digits, add the digits of the
digits. For example, 1234567890 should be 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 0.

For example:
sum_digits(123) = 6
sum_digits(100000000) = 1
sum_digits(42) = 6

Include these tokens in the code: if x < 0 : return 0
"""

def sum_digits(x):
    if x < 0:
        return 0
    else:
        sum_num = 0
        while x > 0:
            sum_num += x % 10
            x = x // 10
        return sum_num

#print(sum_digits(123))
#print(sum_digits(100000000))
#print(sum_digits(42))


# 3.

"""
Write a function that takes a positive integer x and returns the sum of all
odd digits of x. If a number has more than 9 digits, add the digits of the
digits. For example, 1234567890 should be 1 + 3 + 5 + 7 + 9.

For example:
odd_sum(123) = 6
odd_sum(100000000) = 1
odd_sum(42) = 4

Include these tokens in the code: if x < 0