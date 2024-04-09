def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    for prime in primes:
        if a % prime == 0:
            a = a / prime
        else:
            return False

    return True


print(is_multiply_prime(30))
print(is_multiply_prime(15))
print(is_multiply_prime(10))
print(is_multiply_prime(3))
print(is_multiply_prime(17))
print(is_multiply_prime(33))


































































