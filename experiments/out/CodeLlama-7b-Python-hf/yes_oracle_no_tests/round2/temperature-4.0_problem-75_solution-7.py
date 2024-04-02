def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # TODO: Write code here
    
    prime_list = [2,3,5,7,11,13,17,19,23,29]
    for x in prime_list:
        if a % x == 0:
            a = a / x
            if a == 1:
                return True
            else:
                return False

is_multiply_prime(30)