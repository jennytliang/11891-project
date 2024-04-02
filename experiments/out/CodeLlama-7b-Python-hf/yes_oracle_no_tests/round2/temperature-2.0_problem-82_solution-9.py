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
    # First, we must check if the string is empty, if it is, we return False
    if string == "" or string == " ":
        return False
    # We set a counter variable to 1
    counter = 1
    # We set a string length variable to 0
    string_length = 0
    # We set a prime variable to False
    prime = False
    # We set the string length variable to the length of the string
    string_length = len(string)
    # We loop while the counter variable is less than the string length
    while counter < string_length:
        # If the counter variable is equal to 2 or 5, we set the prime variable to True
        if counter == 2 or counter == 5:
            prime = True
        # We set the counter variable to the counter variable plus 1
        counter += 1
    # We return the prime variable
    return prime
