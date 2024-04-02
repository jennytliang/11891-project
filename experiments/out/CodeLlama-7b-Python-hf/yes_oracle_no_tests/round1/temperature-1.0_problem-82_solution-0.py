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
    prime_count = 0
    for i in range ( 1,len ( string )+ 1 ):
        if ( len ( string ) % i == 0 ):
            prime_count += 1
    if ( prime_count == 2 ):
        return True
    else:
        return False

print(prime_length('Hello') == True)
print(prime_length('abcdcba') == True)
print(prime_length('kittens') == True)
print(prime_length('orange') == False)



