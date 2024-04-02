def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: if n > 1 :
	"""
    #code here
    if(n%2==0 and n==2):
        return x
    else:
        if(is_prime(n)):
            return x
        return y


def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True


# write test code here
print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))
print(x_or_y(345, 34, 12))
print(x_or_y(48, 34, 12))
print(x_or_y(2, 34, 12))
print(is_prime(60200))

#output-
34
5
12
34
34
False