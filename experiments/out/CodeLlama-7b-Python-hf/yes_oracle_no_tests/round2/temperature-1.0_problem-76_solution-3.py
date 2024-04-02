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
    return n ** int(round(x**(1 / n))) == x


# def is_simple_power(x, n):
#     assert isinstance(x, int)  # x is integer
#     assert isinstance(n, int)  # n is integer
#     return n ** int(round(x**(1 / n))) == x


if __name__ == '__main__':
    print("Example:")
    print(is_simple_power(1, 1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_simple_power(1, 1) == True
    assert is_simple_power(256, 2) == True
    assert is_simple_power(0, 0) == True
    assert is_simple_power(10, 3) == False
    assert is_simple_power(2, 7) == False
    assert is_simple_power(16, 5) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
