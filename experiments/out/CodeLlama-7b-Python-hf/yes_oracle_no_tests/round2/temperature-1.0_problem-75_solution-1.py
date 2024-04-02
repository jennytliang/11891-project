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
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True
        
def is_multiply_prime(a):
    if a <= 100:
        for num in range(2, a):
            if is_prime(num) == True:
                a = a / num
                return True
            else:
                return False