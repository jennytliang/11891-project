def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 100:
        i = 0
        j = 0
        k = 0
        while i < a:
            i += 1
            j = 2
            while j < a:
                j += 1
                k = 3
                while k < a:
                    k += 1
                    if i * j * k == a:
                        return True
        return False
