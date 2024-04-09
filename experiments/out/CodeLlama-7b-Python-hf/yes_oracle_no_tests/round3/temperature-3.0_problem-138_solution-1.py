def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: and n == ( n // 2 ) ** 2
	"""


    return n >= 8 and n % 2 == 0


if __name__ == '__main__':
    print(is_equal_to_sum_even(4))
    print(is_equal_to_sum_even(6))
    print(is_equal_to_sum_even(8))
    print(is_equal_to_sum_even(10))
    print(is_equal_to_sum_even(12))
    print(is_equal_to_sum_even(14))
    print(is_equal_to_sum_even(16))
    print(is_equal_to_sum_even(18))
    print(is_equal_to_sum_even(20))
    print(is_equal_to_sum_even(22))
    print(is_equal_to_sum_even(24))
    print(is_equal_to_sum_even(26))
    print(is_equal_to_sum_even(28))
    print(is_equal_to_sum_even(30))
    print(is_equal_to_sum_even(32))
    print(is_equal_to_sum_even(34))
    print(is_equal_to_sum_even(36))
    print(is_equal_to_sum_even(38))
    print(is_equal_to_sum_even(40))
    print(is_equal_to_sum_even(42))
    print(is_equal_to_sum_even(44))
    print(is_equal_to_sum_even(46))
    print(is_equal_to_sum_even(48))
    print(is_equal_to_sum_even(50))
    print(is_equal_to_sum_even(52))
    print(is_equal_to_sum_even(54))
    print(is_equal_to_sum_even(56))
    print(is_equal_to_sum_even(58))
    print(is_equal_to_