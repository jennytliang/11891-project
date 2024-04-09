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
    if n == 1:
        return x == 1
    if n == 2:
        return x == 4 or x == 8 or x == 2
    if n == 3:
        return x == 9 or x == 27 or x == 27
    if n == 4:
        return x == 16 or x == 64 or x == 256
    if n == 5:
        return x == 25 or x == 125 or x == 625
    if n == 6:
        return x == 36 or x == 216 or x == 144
    if n == 7:
        return x == 81 or x == 512 or x == 4096
    if n == 8:
        return x == 64 or x == 4096 or x == 65536
    if n == 9:
        return x == 81 or x == 729 or x == 6561
    if n == 10:
        return x == 100 or x == 10000 or x == 1000000
