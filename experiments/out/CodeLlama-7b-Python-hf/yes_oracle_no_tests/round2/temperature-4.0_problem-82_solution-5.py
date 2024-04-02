def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ):
	Do not include these tokens in the code: # write your code below
	"""
    def is_prime(a):
        if a < 2:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    return is_prime(len(string))


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
