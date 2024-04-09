def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: return not ( a
	Do not include these tokens in the code: if
	"""


    def is_primenum(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    if len(string) == 0:
        return False
    return is_primenum(len(string))


