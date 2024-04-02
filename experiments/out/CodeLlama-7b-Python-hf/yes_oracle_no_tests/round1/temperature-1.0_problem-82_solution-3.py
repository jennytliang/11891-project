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
    # pass
    if len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7 or len(string) == 11:
        return True
    elif len(string) == 4 or len(string) == 6 or len(string) == 8 or len(string) == 9 or len(string) == 10:
        return False
    else:
        for i in range(2, len(string)):
            if len(string) % i == 0:
                return False
        return True


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
