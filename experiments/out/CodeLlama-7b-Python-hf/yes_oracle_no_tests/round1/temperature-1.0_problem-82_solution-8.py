def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    #First, make a list of numbers from 2 to the square root of the number whose length
    #you are checking: 
    #def is_prime(n): 
    #    return all(n%i for i in range(2, int(n**0.5)+1))
    numstring = string
    ln = len(numstring)
    primecheck = []
    if len(numstring) == 2:
        primecheck.extend(True)
    else: 
        for num in range(2,ln):
            if len(numstring)%num == 0:
                primecheck.extend(False)
            else:
                primecheck.extend(True)
    if True in primecheck:
        return False
    else:
        return True
                
                   
                
#print(is_prime(13))
#print(is_prime(15))
#print(is_prime(21))