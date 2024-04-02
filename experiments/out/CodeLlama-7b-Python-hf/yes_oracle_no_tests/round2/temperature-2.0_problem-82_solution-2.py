def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Do not include these tokens in the code: # pass # return
	"""
    # pass
    # return
    
    string_length = len(string)
    if string_length == 2:
        return False
    elif string_length == 3:
        return True
    
    for i in range(2, string_length):
        if string_length % i == 0:
            return False
    return True

print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
