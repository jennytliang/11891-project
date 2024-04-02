def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 3:
        return False
    for i in range(2, 100):
        if a % i == 0:
            return is_prime(i) and is_prime(a/i) and is_prime(a/(i*a/i))
    return False


def is_prime(a):
    """Return True if a is prime number and False otherwise."""
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_multiply_prime(30))
    print(is_multiply_prime(31))
    print(is_multiply_prime(27))
    print(is_multiply_prime(10))
    print(is_multiply_prime(2))
    print(is_multiply_prime(25))
