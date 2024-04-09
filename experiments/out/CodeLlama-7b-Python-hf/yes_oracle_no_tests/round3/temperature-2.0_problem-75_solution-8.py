def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    
    # Check if the number is prime
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    # Check if the number is the product of 3 prime numbers
    for i in range(2, a//2):
        if a % i == 0:
            if is_prime(i):
                a = a / i
                if a % i == 0:
                    if is_prime(a):
                        return True
    return False


print(is_multiply_prime(30))
print(is_multiply_prime(25))
print(is_multiply_prime(100))
print(is_multiply_prime(12))
