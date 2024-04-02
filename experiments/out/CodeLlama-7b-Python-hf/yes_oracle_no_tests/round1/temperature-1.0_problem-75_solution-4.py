def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    #check if number is less then 100
    if a <= 100:
        #check for first prime
        for i in range(1,100):
            prime = True
            for j in range(2,i):
                if i%j == 0:
                    prime = False
            if prime:
                break
        #check if second prime
        for i in range(2,100):
            prime = True
            for j in range(2,i):
                if i%j == 0:
                    prime = False
            if prime:
                break
        #check if third prime
        for i in range(2,100):
            prime = True
            for j in range(2,i):
                if i%j == 0:
                    prime = False
            if prime:
                break
        #if all are primes return true
        if prime:
            return True
        else:
            return False
    else:
        return False
            
            