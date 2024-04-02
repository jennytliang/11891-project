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
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: n
	"""

    if n == 1:
        return x == 1
    return x == n ** int(x ** (1 / n))


if __name__ == '__main__':
    print("Example:")
    print(is_simple_power(1, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")