def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    if a < 100:
        is_prime = True
        for i in range(2, 10):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        is_prime = False
        return is_prime
    else:
        return False
