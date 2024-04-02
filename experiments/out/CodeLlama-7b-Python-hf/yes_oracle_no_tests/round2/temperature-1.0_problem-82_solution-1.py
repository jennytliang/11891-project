def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    return None



# TWO FUNCTIONS

import math

def is_prime(num):
    if num > 1:
        for i in range(2, 1 + math.floor(math.sqrt(num))):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

    
def prime_length(string):
    
    return is_prime((len(string)))