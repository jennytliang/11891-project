def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    if a <= 100:
        for i in range(2,a+1):
            prime = True
            for j in range(2,i):
                if i % j == 0:
                    prime = False
            if prime:
                counter = 1
                while counter < 3:
                    for k in range(2,i):
                        if i % k == 0:
                            counter += 1
                    counter = 1
            if counter == 3:
                return True
        return False
    return False



print(is_multiply_prime(30))