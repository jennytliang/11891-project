def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 4 and n % 2 == 0


def test_is_equal_to_sum_even():
    assert not is_equal_to_sum_even(4)
    assert not is_equal_to_sum_even(6)
    assert is_equal_to_sum_even(8)


if __name__ == '__main__':
    test_is_equal_to_sum_even()
