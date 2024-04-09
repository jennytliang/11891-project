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
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return False
        return True

    if a <= 3:
        return True
    else:
        for i in range(2, int(a/2)+1):
            if a % i == 0:
                if is_prime(i):
                    return True
        return False


print(is_multiply_prime(30))