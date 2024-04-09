def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""


    if 0 < a < 100:
        for i in range(a):
            if is_prime(i):
                for j in range(a):
                    if is_prime(j):
                        for k in range(a):
                            if is_prime(k):
                                if i * j * k == a:
                                    return True
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            return False
    else:
        return False



def is_prime(a):
    """Write a function that returns True if a given number (a) is prime and False otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_prime(3) == True
    3 is prime.
    Example:
    is_prime(4) == False
    4 is not prime.
    """
    if 0 < a < 100:
        for i in range(2, a):
            if a % i == 0:
                return False
        else:
            return True
    else:
        return False

def is_prime_for(a):
    """Write a function that returns True if a given number (a) is prime and False otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_prime(3) == True
    3 is prime.
    Example:
    is_prime(4) == False
    4 is not prime.
    """
    if 0 < a < 100:
        for i in range(2, a):
            if a % i == 0:
                return False
        else:
            return True
    else:
        return False































































