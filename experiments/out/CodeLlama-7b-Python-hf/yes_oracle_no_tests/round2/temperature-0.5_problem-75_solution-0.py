def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: is prime
	"""


    if a  <= 1:
        r = False
    elif a == 2 or a == 3:
        r = True
    elif a % 2 == 0 or a % 3 == 0:
        r = False
    else:
        i = 5
        while i * i <= a:
            if a % i == 0:
                r = False
                break
            i += 2
            if i % 3 == 0:
                i += 4
        else:
            r = True
    return r


print(is_multiply_prime(30))
print(is_multiply_prime(25))
print(is_multiply_prime(24))
print(is_multiply_prime(17))
print(is_multiply_prime(16))
