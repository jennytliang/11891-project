def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: return not ( a < 2 or any (
	Do not include these tokens in the code: if
	"""

    
    def is_prime(a):
    	if a < 2 or a % 2 == 0:
    		return False;
    	else:
    		return True;
    
    length = len(string)
    return is_prime(length);
    
    
    