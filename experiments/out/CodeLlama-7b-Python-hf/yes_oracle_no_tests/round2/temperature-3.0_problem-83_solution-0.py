def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # 1 digit numbers that start or end with 1
    one_digit = 1
    # 2 digit numbers that start or end with 1
    two_digit_one = 1
    # 3 digit numbers that start or end with 1
    three_digit_one = 1
    # 4 digit numbers that start or end with 1
    four_digit_one = 1
    # 5 digit numbers that start or end with 1
    five_digit_one = 1
    # 6 digit numbers that start or end with 1
    six_digit_one = 1
    # 7 digit numbers that start or end with 1
    seven_digit_one = 1
    # 8 digit numbers that start or end with 1
    eight_digit_one = 1
    # 9 digit numbers that start or end with 1
    nine_digit_one = 1
    # 10 digit numbers that start or end with 1
    ten_digit_one = 1
    if n == 1:
        return one_digit
    elif n == 2:
        return two_digit_one + one_digit
    elif n == 3:
        return three_digit_one + two_digit_one + one_digit
    elif n == 4:
        return four_digit_one + three_digit_one + two_digit_one + one_digit
    elif n == 5:
        return five_digit_one + four_digit_one + three_digit_one + two_digit_one + one_digit
    elif n == 6:
        return six_digit_one + five_digit_one + four_digit_one + three_digit_one + two_digit_one + one_digit
    elif n == 7:
        return seven_digit_one + six_digit_one + five_digit_one + four_digit_one + three_digit_one + two_digit_one + one_digit
    elif n == 8:
        return eight_digit_one + seven_digit_one + six_digit_one + five_digit_one + four_digit