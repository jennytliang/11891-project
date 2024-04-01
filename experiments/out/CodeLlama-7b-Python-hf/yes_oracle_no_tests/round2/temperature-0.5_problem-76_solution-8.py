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
    
	Include these tokens in the code: if n == 0 : return x ==
	Do not include these tokens in the code: elif
	"""


    if x == 1:
        r = 0
    else:
        r = int(x ** (1/float(n)))
    return r ** n == x



def is_simple_power_v2(x, n):
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
    
	Include these tokens in the code: if n == 0 : return x ==
	Do not include these tokens in the code: elif
	"""


    return x == 1 or int(x**(1/float(n)))**n == x



print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))

print(is_simple_power_v2(1, 4))
print(is_simple_power_v2(2, 2))
print(is_simple_power_v2(8, 2))
print(is_simple_power_v2(3, 2))
print(is_simple_power_v2(3, 1))
print(is_simple_power_v2(5, 3))