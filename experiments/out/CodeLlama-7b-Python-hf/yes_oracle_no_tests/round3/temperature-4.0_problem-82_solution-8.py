def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: not ( a <
	"""

    def is_prime(a):
        r = range(2, a)
        for i in r:
            if a % i == 0:
                return False
        return True

    return is_prime(len(string))
