def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # Initialize variables
    is_multiply_prime = False
    i = 2
    
    # Check if a is multiplied by 3 prime numbers
    while i <= a/3 and not is_multiply_prime:
        if is_prime(i):
            j = 2
            while j <= a/i and not is_multiply_prime:
                if is_prime(j):
                    k = 2
                    while k <= a/(i*j) and not is_multiply_prime:
                        if is_prime(k):
                            if a == i*j*k:
                                is_multiply_prime = True
                        k += 1
                j += 1
        i += 1
    
    return is_multiply_prime

def is_prime(a):
    """Write a function that returns True if a number is prime and False otherwise.
    Knowing that a is less then 100.
    Example:
    is_prime(3) == True
    is_prime(4) == False
    is_prime(5) == True
    is_prime(6) == False
    is_prime(7) == True
    """
    # Initialize variables
    is_prime = True
    
    # Check if a is prime
    if a > 1:
        i = 2
        while i <= a - 1 and is_prime:
            if a % i == 0:
                is_prime = False
            i += 1
    else:
        is_prime = False
    
    return is_prime