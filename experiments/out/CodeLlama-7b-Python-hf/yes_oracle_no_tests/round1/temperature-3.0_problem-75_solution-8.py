def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # TODO: write your solution here
    for i in range(1,100):
        for j in range(1,100):
            for k in range(1,100):
                if i * j * k == a:
                    return True
    return False
