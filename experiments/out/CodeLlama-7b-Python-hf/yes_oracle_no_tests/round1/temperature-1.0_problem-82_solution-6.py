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
    
    def is_prime(a):
        if a == 1 or a == 2:
            return True
        for x in range(2,a):
            if a % x == 0:
                return False
        return True
            
    if len(string) == 1 and string == 'a':
        return True

    if is_prime(len(string)):
        return True
    else:
        return False
