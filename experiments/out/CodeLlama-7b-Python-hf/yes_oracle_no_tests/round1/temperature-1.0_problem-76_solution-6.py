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
    assert x > 0
    assert x >= n
    
    if n == 1 and x != 1:
        return False
    
    exp = 0
    
    while (n ** exp) < (x / n + 1e-8):
        
        if x == n ** exp:
            return True
        
        else:
            exp += 1  # increment exponent variable to next higher power
            
            if (n ** exp) > (x + 1e-8): # check if power is too high
                return False


    if x == n ** exp:
            return True
    
    else:
            return False

print(is_simple_power(4096,2))