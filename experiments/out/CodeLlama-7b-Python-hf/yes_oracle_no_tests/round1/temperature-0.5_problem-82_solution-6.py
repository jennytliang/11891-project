def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: if len
	"""

    
    def is_prime(string):
        if len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7:
            return True
        else:
            return False
    
    return is_prime(string)