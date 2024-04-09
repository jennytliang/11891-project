def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # your code here
	"""
    # Write your code here
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    if a == 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a%i == 0:
            if not is_prime(i):
                return False
    return True

print(is_multiply_prime(30))