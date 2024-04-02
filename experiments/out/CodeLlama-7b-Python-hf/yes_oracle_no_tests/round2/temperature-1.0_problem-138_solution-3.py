def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: 8 and n % 2 == 0
	Do not include these tokens in the code: 4
	"""

    return 4-len(list(filter(lambda v: n%2==0,{10, 8, 6, 2, 4, 20, 12, 44,}) ))==0


def test_is_equal_to_sum_even():

    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(8) == True
