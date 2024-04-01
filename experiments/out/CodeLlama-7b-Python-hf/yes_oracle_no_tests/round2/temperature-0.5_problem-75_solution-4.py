def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: is prime = [ True ] * ( a +
	"""


    if a  <= 1:
        r = False
    else:
        r = True
        for i in range(2, a):
            if a % i == 0:
                if is_prime(i) == True:
                    r = True
                else:
                    r = False
                    break
            else:
                r = False
                break
    return r


def is_prime(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_prime(7) == True
    is_prime(30) == False
    """
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True


def is_product_three_prime(n):
    """Write a function that returns true if the given number is the product of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_product_three_prime(30) == True
    30 = 2 * 3 * 5
    """
    if n <= 1:
        return False
    else:
        for i in range(1, n):
            if is_prime(i) == True:
                for j in range(1, n):
                    if is_prime(j) == True:
                        for k in range(1, n):
                            if is_prime(k) == True:
                                if i * j * k == n:
                                    return True
    return False


def is_product_three_prime_2(n):
    """Write a function that returns true if the given number is the product of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then