def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: return not ( a < 2 or any (
	"""


    def is_prime(a):
 
        # Corner cases
        if a <= 1:
            return False
 
        # Iterate from 2 to n / 2
        for i in range(2, a):
            if (a % i) == 0:
                return False
 
        return True
 
    length = len(string)
    
    return is_prime(length)
