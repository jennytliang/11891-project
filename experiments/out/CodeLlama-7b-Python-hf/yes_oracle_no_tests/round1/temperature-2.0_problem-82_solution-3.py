def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: length = len
	"""
    def is_prime(n):
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True

    res = is_prime(len(string))
    return res

print(prime_length('Hello') == True)
print(prime_length('abcdcba') == True)
print(prime_length('kittens') == True)
print(prime_length('orange') == False)
