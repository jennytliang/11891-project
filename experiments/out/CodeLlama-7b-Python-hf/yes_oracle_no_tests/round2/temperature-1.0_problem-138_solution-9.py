def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: and n % 2 == 0
	Do not include these tokens in the code: # TO DO : implement this method
	"""

    return n % 2 == 0


def test_is_equal_to_sum_even():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(8) == True


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: and n % 2 == 1
	Do not include these tokens in the code: # TO DO : implement this method
	"""

    return n % 2 == 1


def test_is_equal_to_sum_odd():
    assert is_equal_to_sum_odd(4) == False
    assert is_equal_to_sum_odd(6) == True
    assert is_equal_to_sum_odd(8) == False


def is_equal_to_sum_two_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers
    Example
    is_equal_to_sum_two_even(4) == False
    is_equal_to_sum_two_even(6) == False
    is_equal_to_sum_two_even(8) == True
    
	Include these tokens in the code: and n % 2 == 0
	Do not include these tokens in the code: # TO DO : implement this method
	"""

    return n % 2 == 0


def test_is_equal_to_sum_two_even():
    assert is_equal_to_sum_two_even(4) == False
    assert is_equal_to_sum_two_even(6) == False
    assert is_equal_to_sum