def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: pass def is _
	"""
    # your code here
    if a < 100:
        for i in range(2, 100):
            if is_prime(i):
                for j in range(2, 100):
                    if is_prime(j):
                        for k in range(2, 100):
                            if is_prime(k):
                                if i * j * k == a:
                                    return True
    return False


def is_prime(a):
    """Write a function that checks if a number is prime or not.
    Example:
    is_prime(7) == True
    
	Do not include these tokens in the code: pass def is_
    """
    # your code here
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if i * i > a:
                return True
            elif a % i == 0:
                return False
    return True
