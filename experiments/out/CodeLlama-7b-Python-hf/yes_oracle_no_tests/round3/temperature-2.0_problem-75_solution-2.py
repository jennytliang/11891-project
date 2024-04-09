def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 30:
        for i in range(1, a+1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    count = 0
                    for k in range(1, i):
                        if (i % k) == 0:
                            count += 1
                            if count == 3:
                                return True
                    if count == 2:
                        return True
    else:
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
    if a <= 30:
        for i in range(1, a+1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    count = 0
                    for k in range(1, i):
                        if (i % k) == 0:
                            count += 1
                            if count == 3:
                                return True
                    if count == 2:
                        return True
    else:
        return False


# print(is_multiply_prime(30))
# print(is_multiply_prime_2(30))


def is_prime(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_prime(3) == True
    is_prime(30) == False
    
	Include these tokens in the code: if a <=
	