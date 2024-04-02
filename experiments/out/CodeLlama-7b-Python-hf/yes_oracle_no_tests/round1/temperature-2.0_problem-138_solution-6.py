def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    total = 0
    for i in range(1, n):
        if i % 2 == 0:
            total += i
            if total == n:
                return True
    return False


print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(9))
print(is_equal_to_sum_even(10))
print(is_equal_to_sum_even(15))
print(is_equal_to_sum_even(16))
print(is_equal_to_sum_even(17))
print(is_equal_to_sum_even(18))
print(is_equal_to_sum_even(19))
print(is_equal_to_sum_even(20))
print(is_equal_to_sum_even(21))
print(is_equal_to_sum_even(22))
print(is_equal_to_sum_even(23))
print(is_equal_to_sum_even(24))
print(is_equal_to_sum_even(25))
print(is_equal_to_sum_even(26))
print(is_equal_to_sum_even(27))
print(is_equal_to_sum_even(28))
print(is_equal_to_sum_even(29))
print(is_equal_to_sum_even(30))
print(is_equal_to_sum_even(31))
print(is_equal_to_sum_even(32))
print(is_equal_to_sum_even(33))
print(is_equal_to_sum_even(34))
print(is_equal_to_sum_even(35))
print(is_equal_to_sum_even(36))
print(is_equal_to_sum_even(37))
print(is_equal_to_sum_even(38))
print(is_equal_to_sum_even(39))
print(is_