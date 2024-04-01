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
    
	Do not include these tokens in the code: x %
	"""


    if x == 1:
        retu = True
    else:
        retu = False
        if x == n:
            retu = True
        else:
            while x > 1:
                x = x / n
                if x == 1:
                    retu = True
                else:
                    retu = False
    return retu


def is_simple_power(x, n):
    return x == n**int(x / n)
