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
	if len(string) == 1:
		return True
	elif len(string) == 2:
		return False
	else:
		temp = 2
		counter = 1
		while counter < len(string):
				if temp % counter == 0 and temp != counter:
					counter += 1 # this will let you check the next prime
				elif temp != counter and counter == len(string):
					return True
				else:
					return False