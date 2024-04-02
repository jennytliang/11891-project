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
    return x == n**int(x/n)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_simple_power(1, 4) == True, "1st example"
    assert is_simple_power(2, 2) == True, "2nd example"
    assert is_simple_power(8, 2) == True, "3rd example"
    assert is_simple_power(3, 2) == False, "4th example"
    assert is_simple_power(3, 1) == False, "5th example"
    assert is_simple_power(5, 3) == False, "6th example"
