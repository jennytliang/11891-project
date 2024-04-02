def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Do not include these tokens in the code: import math
	"""
    return isprime(len(string))
    
def isprime(number):
    if number == 1:
        return False
    
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


# Tests
assert (prime_length('Hello')) == True, "Should be True"
assert (prime_length('abcdcba')) == True, "Should be True"
assert (prime_length('kittens')) == True, "Should be True"
assert (prime_length('orange')) == False, "Should be False"
assert (prime_length('test') == False, "Should be False")