def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    if a <= 100:
        for i in range(2, a):
            if is_prime(i) and is_prime(a / i):
                if is_prime(a / (i * (a / i))):
                    return True
        return False
    return False


print(is_multiply_prime(30))

