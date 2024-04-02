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
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return False
    elif len(string) % 2 == 0:
        return False
    else:
        for i in range(3, len(string)+1, 2):
            if len(string) % i == 0:
                return False
            else:
                return True


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
