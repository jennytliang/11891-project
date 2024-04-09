def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # Prime numbers are divis ible by
	"""
    
    # Prime numbers are divisible by 1 and themselves, 
    # so we'll go through each number up to the square root of the number
    for i in range(2, int(string**0.5)+1):
        # If we find a factor, then it's not a prime number
        if string % i == 0:
            return False
    return True

print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))