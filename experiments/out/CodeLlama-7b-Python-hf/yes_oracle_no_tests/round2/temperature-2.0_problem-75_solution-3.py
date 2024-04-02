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
        if a == 2:
            return True
        else:
            for i in range(2,a):
                if a % i == 0:
                    for j in range(2,i):
                        if i % j == 0:
                            return False
                        else:
                            return True
                else:
                    return False
    else:
        return False


print(is_multiply_prime(30))
