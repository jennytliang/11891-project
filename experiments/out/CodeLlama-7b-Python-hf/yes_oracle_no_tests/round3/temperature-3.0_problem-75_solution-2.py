def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    for i in range(2,a):
        if a % i != 0:
            continue
        else:
            for j in range(2,i):
                if i % j != 0:
                    continue
                else:
                    for k in range(2,j):
                        if j % k != 0:
                            continue
                        else:
                            return True
    return False



def is_multiply_prime_2(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    count = 0
    for i in range(2,a):
        if a % i != 0:
            continue
        else:
            for j in range(2,i):
                if i % j != 0:
                    continue
                else:
                    for k in range(2,j):
                        if j % k != 0:
                            continue
                        else:
                            count += 1
    if count == 3:
        return True
    return False















































































































































































