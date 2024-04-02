def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if
	Do not include these tokens in the code: pass def is _
	"""
    if a < 100:
        for i in range(2,a):
            for j in range(2,i):
                if i % j == 0 and i != j:
                    return False
        return True
    else:
        return False


print(is_multiply_prime(100))
