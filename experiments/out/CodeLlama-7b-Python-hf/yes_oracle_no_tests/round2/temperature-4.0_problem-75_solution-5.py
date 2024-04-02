def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    if a == 0:
        return False

    if a == 2 or a == 3 or a == 5:
        return True

    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False

    if a < 20:
        return False

    if a < 31:
        return True

    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True
