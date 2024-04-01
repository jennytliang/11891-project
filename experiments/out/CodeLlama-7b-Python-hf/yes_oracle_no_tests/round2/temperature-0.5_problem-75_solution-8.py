def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: i
	"""


    if a  <= 1:
        r = False
    else:
        r = True
    
    for i in range(2, a):
        if (a % i) == 0:
            r = False
            break   
    return r



def is_prime(a):
    """Write a function that returns true if the given number is prime and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_prime(30) == False
    30 = 2 * 3 * 5
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: i
	"""
    r = True
    if a  <= 1:
        r = False
    else:
        for i in range(2, a):
            if (a % i) == 0:
                r = False
                break   
    return r



def sum_of_divisors(a):
    """Write a function that returns the sum of all divisors of a given number.
    Knowing that (a) is less then 100.
    Examples:
    sum_of_divisors(220) == 284
    
	Include these tokens in the code: sum of divisors
	Do not include these tokens in the code: i
	"""
    r = 0
    for i in range(1, a):
        if (a % i) == 0:
            r += i
    return r



def divisors(a):
    """Write a function that returns the number of all divisors of the given number.
    Knowing that (a) is less then 100.
    Examples:
    divisors(220) == 8
    
	Include these tokens in the code: number of divisors
	Do not include these tokens in the code: i
	"""
    r = 0
    for i in range(1, a):
        if (a % i) == 0:
            r += 1
    return r



def is_prime_power(a):
