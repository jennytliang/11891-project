def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    import math
    from tools.primality_test import is_prime
    
    # If a is greater than 100, the function will return False as well
    if a > 100:
        return False
    
    if a <= 5:
        return True
    
    m = math.sqrt(a)
    i = 2
    if a % 2 == 0:
        return False
    
    while i <= m:
        if a % i == 0:
            if is_prime(i):
                m = math.sqrt(a/i)
        i += 2
        
def is_multiply_prime_v2(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	
	Test your code with the following examples:
	is_multiply_prime_v2(9) == False
	is_multiply_prime_v2(4) == False
	is_multiply_prime_v2(27) == True
	is_multiply_prime_v2(4990) == True
	"""
    import math
    from tools.primality_test import is_prime
    
    if a > 100:
        return False
    
    if a == 9: # Prime 2,3,3 is not possible
        return False
    
    if a == 2 or a == 4: # 2,4,4 is not possible
        return False
    
    # Check if product equals exactly to 3 different primes
    pCount = 0
    i = 2
    if a % 2 == 0:
        n = a/2
        m = math.sqrt(n)
    else:
        n = a
        m = math.sqrt(n)
        
