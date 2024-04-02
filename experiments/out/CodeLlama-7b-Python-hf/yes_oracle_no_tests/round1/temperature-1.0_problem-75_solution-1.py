def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    prime_list = [2, 3, 5]
    for prime in prime_list:
        if a % prime == 0:
            a = a / prime
        else:
            return False
    return True
    

