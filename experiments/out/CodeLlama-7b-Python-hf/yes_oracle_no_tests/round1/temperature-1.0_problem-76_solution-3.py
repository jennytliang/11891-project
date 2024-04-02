def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    
	Include these tokens in the code: if x ==
	"""
    return x == n ** int(x / n)


def test_function():
    assert is_simple_power(1, 4) == True, "First"
    assert is_simple_power(2, 2) == True, "Second"
    assert is_simple_power(8, 2) == True, "Third"
    assert is_simple_power(3, 2) == False, "Fourth"
    assert is_simple_power(3, 1) == False, "Fifth"
    assert is_simple_power(5, 3) == False, "Sixth"
    assert is_simple_power(16, 2) == True, "Seventh"
    assert is_simple_power(27, 3) == False, "Eighth"
    assert is_simple_power(32, 5) == True, "Ninth"
    assert is_simple_power(1, 1) == True, "Tenth"
