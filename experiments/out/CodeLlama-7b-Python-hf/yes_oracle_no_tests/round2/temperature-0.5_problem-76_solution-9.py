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
    
	Include these tokens in the code: if n == 0 :
	"""


    if x == 1:
        r = 0
    else:
        r = n
        while r <= x:
            if r ** 2 == x:
                break
            r += 1

    if r ** 2 == x:
        return True
    else:
        return False
