def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # 1 is not a prime number
    if a == 1:
        return False
    # 2 is a prime number
    if a == 2:
        return True
    # 3 is a prime number
    if a == 3:
        return True

    # If a < 2, a is not a prime number
    if a < 2:
        return False

    # If a is not divisible by 2, it is a prime number
    # because all numbers are divisible by 1
    if a % 2 > 0:
        # If a is not divisible by 3, it is a prime number
        # because all numbers are divisible by 1 and 2
        if a % 3 > 0:
            # If a is not divisible by 5, it is a prime number
            # because all numbers are divisible by 1, 2 and 3
            if a % 5 > 0:
                # If a is not divisible by 7, it is a prime number
                # because all numbers are divisible by 1, 2, 3 and 5
                if a % 7 > 0:
                    # If a is not divisible by 11, it is a prime number
                    # because all numbers are divisible by 1, 2, 3, 5, and 7
                    if a % 11 > 0:
                        # If a is not divisible by 13, it is a prime number
                        # because all numbers are divisible by 1, 2, 3, 5, 7, and 11
                        if a % 13 > 0:
                            # If a is not divisible by 17, it is a prime number
                            # because all numbers are divisible by 1, 2, 3, 5, 7, 11, and 13
                            if a % 17 > 0:
                                # If a is not divisible by 19, it is a prime number
                                # because all numbers are divisible by 1, 2,