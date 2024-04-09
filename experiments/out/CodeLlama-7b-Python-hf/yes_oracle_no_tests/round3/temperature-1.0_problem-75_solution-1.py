def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    if a == 0:
        return False
    else:
        p = 2
        while a != 1:
            k = 0
            while a % p == 0:
                k += 1
                a = a / p
            if k > 0:
                p += 1
            else:
                return False
        return True
