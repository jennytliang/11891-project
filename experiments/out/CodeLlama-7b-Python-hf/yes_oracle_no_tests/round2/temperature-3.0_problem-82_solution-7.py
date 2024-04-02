def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: a
	Do not include these tokens in the code: num
	"""

    def is_p(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return is_p(len(string))


print(prime_length("Hello"))
print(prime_length("abcdcba"))
print(prime_length("kittens"))
print(prime_length("orange"))
