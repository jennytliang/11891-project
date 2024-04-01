def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: if a == 2 or a == 3
	"""


    if a  <= 1:
        r = False
    elif a == 2 or a == 3:
        r = True
    else:
        r = False
        for i in range(2, a//2 + 1):
            if a % i == 0:
                r = False
                break
            else:
                r = True
    return r



def is_multiply_prime2(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a  <= 1:
        return False
    elif a == 2 or a == 3:
        return True
    else:
        for i in range(2, a//2 + 1):
            if a % i == 0:
                return False
    return True




def is_multiply_prime3(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a  <= 1:
        return False
    elif a == 2 or a == 3:
        return True
    else:
        return a % 2 != 0 and a % 3 != 0


















































































































