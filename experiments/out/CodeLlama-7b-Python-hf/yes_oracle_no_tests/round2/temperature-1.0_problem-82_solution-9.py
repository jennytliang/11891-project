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
    if len(string) == 2:
        return True
    for num in range(2,len(string)):
        if len(string) % num == 0:
            return False
    return True


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))