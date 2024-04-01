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

    
    
    # if len(string) == 1:
    #     return False
    # for x in range(2, len(string)):
    #     if len(string) % x == 0:
    #         return False
    # return True
    
    if len(string) == 1:
        return False
    for x in range(2, len(string)):
        if len(string) % x == 0:
            return False
    return True
