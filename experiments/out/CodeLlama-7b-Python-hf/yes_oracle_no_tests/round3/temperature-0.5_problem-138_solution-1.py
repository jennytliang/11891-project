def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: def test _ case ( test _ number ,
	"""



    
    return n >= 8 and 2 * n % 2 == 0




def test_cases():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(14) == False
    assert is_equal_to_sum_even(16) == True
    assert is_equal_to_sum_even(18) == False
    assert is_equal_to_sum_even(20) == True
    assert is_equal_to_sum_even(22) == False
    assert is_equal_to_sum_even(24) == True
    assert is_equal_to_sum_even(26) == False
    assert is_equal_to_sum_even(28) == True
    assert is_equal_to_sum_even(30) == False
    assert is_equal_to_sum_even(32) == True
    assert is_equal_to_sum_even(34) == False
    assert is_equal_to_sum_even(36) == True
    assert is_equal_to_sum_even(38) == False
    assert is_equal_to_sum_even(40) == True
    assert is_equal_to_sum_even(42) == False
    assert is_equal_to_sum_even(44) == True
    assert is_equal_to_sum_even(46) == False
    assert is_equal_to_sum_even(48) == True
    assert is_equal_to_sum_even(50) == False
    assert is_equal_to_sum_even(52) == True
    assert is_equal_to_sum_even(54) == False
    assert is_equal_to_sum_even(56)