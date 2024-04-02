def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def
	"""
    def is_prime(num):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    return is_prime(len(string))
