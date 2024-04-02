def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # 1 is not a prime number
    if a <= 1:
        return False
    # 2 is a prime number
    if a == 2:
        return True
    # 3 is a prime number
    if a == 3:
        return True
    # 4 is not a prime number
    if a == 4:
        return False
    # 5 is a prime number
    if a == 5:
        return True
    # 6 is not a prime number
    if a == 6:
        return False
    # 7 is a prime number
    if a == 7:
        return True
    # 8 is not a prime number
    if a == 8:
        return False
    # 9 is not a prime number
    if a == 9:
        return False
    
    # check if a is a prime number
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break

    # check if a is the multiplication of 3 prime numbers
    if is_prime:
        return False

    is_multiply_prime = False
    for i in range(2, a):
        for j in range(2, a):
            if i*j == a:
                is_multiply_prime = True
                break

    return is_multiply_prime


def is_multiply_prime_optimized(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # 1 is not a prime number
    if a <= 1:
        return False
    # 2 is a prime number
    if a == 2:
        return True
    # 3 is a prime number
    if a ==