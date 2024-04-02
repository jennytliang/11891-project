def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # Initialize a variable to store the product of the first 2 prime numbers
    product = 2
    
    # If the first number is not a prime, return false
    if not is_prime(a):
        return False
    
    # If the first number is a prime, check if the product of the first two primes is equal to the number
    if product == a:
        return True
    
    # For each prime number check if the product is equal to the number
    for prime in range(2, a):
        
        # If the product is equal to the number, return true
        if product * prime == a:
            return True
        
        # If the product is not equal to the number, update the product
        product *= prime
        
    # If none of the products is equal to the number, return false
    return False

def is_prime(a):
    """Write a function that returns True if the given number is prime, 
    and False otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_prime(7) == True
    """
    # Create a list of all the numbers from 2 to a
    numbers = list(range(2, a))
    
    # Check if the number is equal to 2, return true
    if a == 2:
        return True
    
    # If the number is not equal to 2, check if it is dividable by 2
    if a % 2 == 0:
        return False
    
    # If the number is not dividable by 2, check if it is dividable by any of the numbers from 3 to the number
    for number in numbers:
        if a % number == 0:
            return False
    
    # If the number is dividable only by 1 and itself, return true
    return True

print(is_multiply_prime(30))