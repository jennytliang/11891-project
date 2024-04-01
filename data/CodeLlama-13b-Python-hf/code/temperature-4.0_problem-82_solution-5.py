def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return len(string) == is_prime(len(string))
    
	#or
#    return all(chr(key).isdigit() is key != 1 for key in list(range(2, len(string))))
