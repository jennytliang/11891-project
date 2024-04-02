def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: pr imes
	"""
    # write your code below
    if string == '':
        return False
    else:
        length = len(string)
        if length == 1:
            return True
        for i in range(2, length):
            if length % i == 0:
                return False
        return True

print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
print(prime_length(''))
print(prime_length('1'))
print(prime_length('2'))
print(prime_length('3'))
print(prime_length('4'))
print(prime_length('5'))