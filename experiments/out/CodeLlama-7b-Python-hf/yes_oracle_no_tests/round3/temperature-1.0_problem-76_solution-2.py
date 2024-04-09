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
    
	Include these tokens in the code: 1 :
	Do not include these tokens in the code: n ** int ( x / n ):
	"""


    i = 1
    while i < x:
        if i ** n == x:
            return True
        i += 1
    return False

if __name__ == '__main__':
    print("Example:")
    print(is_simple_power(1, 4))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_simple_power(1, 4) == True
    assert is_simple_power(2, 2) == True
    assert is_simple_power(8, 2) == True
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False
