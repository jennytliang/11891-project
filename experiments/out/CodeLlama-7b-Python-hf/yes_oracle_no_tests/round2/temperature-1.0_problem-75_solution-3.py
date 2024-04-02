def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: if a <= 3 :
	"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes:
        if a % prime == 0:
            a = a / prime
        else:
            continue
    return a == 1


assert is_multiply_prime(2 * 3 * 5) == True
assert is_multiply_prime(10) == False
assert is_multiply_prime(30) == True
assert is_multiply_prime(32) == False
assert is_multiply_prime(1) == False
assert is_multiply_prime(2) == False
assert is_multiply_prime(3) == False
assert is_multiply_prime(4) == False
assert is_multiply_prime(5) == False
assert is_multiply_prime(6) == False
assert is_multiply_prime(7) == False
assert is_multiply_prime(8) == False
assert is_multiply_prime(9) == False
assert is_multiply_prime(10) == False
