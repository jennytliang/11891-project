def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # 1. Check if a is prime
    # 2. If a is prime, check if a is the product of 3 prime numbers
    # 3. If a is not prime, return false
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if a <= 100:
        for prime in primes:
            if a % prime == 0:
                return True
    return False


print(is_multiply_prime(30))
print(is_multiply_prime(40))
print(is_multiply_prime(70))
print(is_multiply_prime(80))
print(is_multiply_prime(90))
print(is_multiply_prime(91))
print(is_multiply_prime(92))
print(is_multiply_prime(93))
print(is_multiply_prime(94))
print(is_multiply_prime(95))
print(is_multiply_prime(96))
print(is_multiply_prime(97))
print(is_multiply_prime(98))
print(is_multiply_prime(99))
print(is_multiply_prime(100))
