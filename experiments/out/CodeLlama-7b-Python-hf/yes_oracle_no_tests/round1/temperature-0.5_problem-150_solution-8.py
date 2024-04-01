def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n >  1 :
	"""

    
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    Examples:
    for is_prime(3) == True
    for is_prime(8) == False
    """
    # Your code here
    if n == 2:
        return True
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


print(x_or_y(15, 8, 5))
print(x_or_y(7, 34, 12))
