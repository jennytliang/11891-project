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
        for i in range(2, a):
            if a % i == 0:
                if is_prime(i):
                    for j in range(2, a):
                        if a % j == 0:
                            if is_prime(j):
                                for k in range(2, a):
                                    if a % k == 0:
                                        if is_prime(k):
                                            return True
    return False

def is_prime(a):
    if a <= 100:
        for i in range(2, a):
            if a % i == 0:
                return False
    return True







