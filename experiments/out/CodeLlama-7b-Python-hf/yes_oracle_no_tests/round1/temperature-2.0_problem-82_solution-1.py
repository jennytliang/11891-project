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
    
    def is_prime(string):
        """
        Args:
            string (str):

        Returns:
            bool: True if prime, False otherwise
        """
        if len(string) == 1:
            return False
        for i in range(2, len(string)):
            if len(string) % i == 0:
                return False
        return True

    return is_prime(string)

print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))