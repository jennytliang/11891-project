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
        p = 0
        if a == 1:
            return False
        for i in range(1, a + 1):
            if a % i == 0:
                p += 1
        if p == 2:
            return True
        else:
            return False

    return is_prime(len(string))
