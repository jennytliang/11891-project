def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # write code here
	"""
    # 1. Check if a is a multiple of 2
    # 2. If it is not, check if it is a multiple of 3
    # 3. If it is not, check if it is a multiple of 5
    # 4. If it is not, then it is not a multiple of 2, 3, or 5
    # 5. If it is a multiple of 2, 3, or 5, check if it is the product of 2 prime numbers
    # 6. If it is the product of 2 prime numbers, return True
    # 7. If it is not, return False
    
    # 1. Check if a is a multiple of 2
    if a % 2 == 0:
        # 2. If it is not, check if it is a multiple of 3
        if a % 3 != 0:
            # 3. If it is not, check if it is a multiple of 5
            if a % 5 != 0:
                # 4. If it is not, then it is not a multiple of 2, 3, or 5
                return False
            # 5. If it is a multiple of 5, check if it is the product of 2 prime numbers
            elif a % 5 == 0:
                # 6. If it is the product of 2 prime numbers, return True
                if (a / 5) % 2 == 0 and (a / 5) % 3 != 0:
                    return True
        # 7. If it is a multiple of 3, check if it is the product of 2 prime numbers
        elif a % 3 == 0:
            # 6. If it is the product of 2 prime numbers, return True
            if (a / 3) % 2 != 0 and (a / 3) % 5 != 0:
                return True
    # 8. If it is a multiple of 2, check if it is the product of 2 prime numbers
    elif a % 2 == 0:
        # 6. If it is the product of 2 prime numbers,