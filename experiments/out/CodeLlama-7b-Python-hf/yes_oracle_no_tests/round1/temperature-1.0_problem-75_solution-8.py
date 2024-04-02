def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    multiplier = 1

    # check if a is under 30, for the example i put. 
    if a <= 30 :
        for x in range( 2 , a ) :
            is_prime = True
            if a % x == 0:
                multiplier += 1
                is_prime = is_prime_number(x)
                if is_prime:
                    if multiplier > 3 :
                        return False
                else:
                    multiplier = 1
                    break
    return False

def is_prime_number(n):
    if not (n % 2) and n != 2:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 2 , 2):
            if n % i == 0:
                return False
    return True

print("Is 30 multiplied by 2 ,3 ,5 == True ? " + str(is_multiply_prime(30)))
print("Is 15 multiplied by 5 ,5 ,5 == True ? " + str(is_multiply_prime(15)))
print("Is 16 multiplied by 2 ,3 , 8 == True ? " + str(is_multiply_prime(16)))