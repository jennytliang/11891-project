def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: # # W R ITE
	"""
    if a <= 100:
        for i in range(2, a):
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
            if prime:
                for k in range(2, i):
                    if i % k == 0:
                        prime = False
            if prime:
                for l in range(2, i):
                    if i % l == 0:
                        prime = False
            if prime:
                return True
        return False
    return False


is_multiply_prime(30)
