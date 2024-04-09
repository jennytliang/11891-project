def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""

    # YOUR CODE HERE
    string = len(string)
    if string < 2:
        return False
    for i in range(2, string):
        if string % i == 0:
            return False
    return True
