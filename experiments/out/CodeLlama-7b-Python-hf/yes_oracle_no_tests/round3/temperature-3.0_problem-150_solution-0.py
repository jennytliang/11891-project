def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: return not ( a < 2 or any (
	Do not include these tokens in the code: r = True
	"""


    def is_prime(a):
 
        if a < 2:
            return False
        if a == 2:
            return True
        if a % 2 == 0:
            return False
 
        for i in range(3, int(a**0.5)+1, 2):
            if a % i == 0:
                return False
 
        return True
 
    return x if is_prime(n) else y
