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
        for i in range(2,a):
            for j in range(2,i):
                if i % j == 0:
                    return False
        return True

def is_multiply_prime_2(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 100:
        count = 0
        for i in range(2,a):
            for j in range(2,i):
                if i % j == 0:
                    count += 1
        if count == 2:
            return True
        return False

#print(is_multiply_prime(30))
#print(is_multiply_prime_2(30))