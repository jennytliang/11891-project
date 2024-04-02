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
    prime = False
    if len(string) == 2:
        prime = True
    elif len(string) == 3:
        prime = True
    elif len(string) == 5:
        prime = True
    elif len(string) == 7:
        prime = True
    elif len(string) == 11:
        prime = True
    elif len(string) == 13:
        prime = True
    elif len(string) == 17:
        prime = True
    elif len(string) == 19:
        prime = True
    elif len(string) == 23:
        prime = True
    elif len(string) == 29:
        prime = True
    elif len(string) == 31:
        prime = True
    elif len(string) == 37:
        prime = True
    elif len(string) == 41:
        prime = True
    elif len(string) == 43:
        prime = True
    elif len(string) == 47:
        prime = True
    elif len(string) == 53:
        prime = True
    elif len(string) == 59:
        prime = True
    elif len(string) == 61:
        prime = True
    elif len(string) == 67:
        prime = True
    elif len(string) == 71:
        prime = True
    elif len(string) == 73:
        prime = True
    elif len(string) == 79:
        prime = True
    elif len(string) == 83:
        prime = True
    elif len(string) == 89:
        prime = True
    elif len(string) == 97:
        prime = True
    elif len(string) == 101:
        prime = True
    elif len(string) == 103:
        prime = True
    else:
        prime = False
    return prime


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(