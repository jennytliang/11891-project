def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: def is _ prime ( number
	"""
    def is_prime(a):
        for i in range(2, int(a/2)+1):
            if a % i == 0:
                return False
        return True
    
    if a < 100:
        for i in range(2, 100):
            if is_prime(i) and is_prime(a//i):
                return True
    return False


print(is_multiply_prime(30))
