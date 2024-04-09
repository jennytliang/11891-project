def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""

    i = 0
    j = 1
    while i < a and j < a:
        while i < a and j < a:
            if j * i == a:
                return True
            j += 1
        i += 1
        j = 1
        return False


print(is_multiply_prime(10))
print(is_multiply_prime(30))
print(is_multiply_prime(100))
print(is_multiply_prime(11))
print(is_multiply_prime(16))
print(is_multiply_prime(17))
print(is_multiply_prime(18))
