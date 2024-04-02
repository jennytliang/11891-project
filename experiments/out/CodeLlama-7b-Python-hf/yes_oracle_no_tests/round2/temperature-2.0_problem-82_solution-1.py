def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: a
	Do not include these tokens in the code: string
	"""

    
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return is_prime(len(string))
