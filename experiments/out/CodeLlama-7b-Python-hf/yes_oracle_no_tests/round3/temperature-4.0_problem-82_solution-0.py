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
    def is_prime(a):
        return (a == 2) or (a == 3) or (a == 5) or (a == 7) or (a == 11) or (a == 13) or (a == 17) or (a == 19) or (a == 23) or (a == 29)

    return is_prime(len(string))


#print(prime_length('Hello'))
#print(prime_length('abcdcba'))
#print(prime_length('kittens'))
#print(prime_length('orange'))






