def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # pass
    even = 0
    odd = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)


# print(even_odd_count(123))
# print(even_odd_count(-12))
# print(even_odd_count(1230))
# print(even_odd_count(-1230))


def get_digit_sum(num1, num2):
    """Given two integers. return the sum of the digits of the larger number.

     Example:
        get_digit_sum(12, 34) ==> 12
        get_digit_sum(123, 34) ==> 123
    
	"""
    # pass
    if num1 > num2:
        return sum(map(int, str(num1)))
    else:
        return sum(map(int, str(num2)))


# print(get_digit_sum(23, 234))
# print(get_digit_sum(123, 34))
# print(get_digit_sum(123, 94))


def get_digit_sum2(num1, num2):
    """Given two integers. return the sum of the digits of the larger number.

     Example:
        get_digit_sum(12, 34) ==> 12
        get_digit_sum(123, 34) ==> 123
    
	"""
    # pass
    return sum(max(str(num1), str(num2)))


# print(get_digit_sum2(23, 234))
# print(get_digit_sum2(123, 34))
# print(get_digit_sum2(123, 94))


def get_digit_sum3(num1, num2):
    """Given two integers