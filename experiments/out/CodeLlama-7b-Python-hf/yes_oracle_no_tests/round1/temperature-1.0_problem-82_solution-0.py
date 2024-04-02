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
        if a < 2:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True
    return is_prime(len(string))


def prime_length_two(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length_two('Hello') == True
    prime_length_two('abcdcba') == True
    prime_length_two('kittens') == True
    prime_length_two('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    def is_prime(a):
        if a < 2:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True
    return is_prime(len(string))
