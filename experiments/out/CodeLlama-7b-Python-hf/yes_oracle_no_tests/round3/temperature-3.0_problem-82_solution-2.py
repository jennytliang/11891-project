def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: prime
	Do not include these tokens in the code: p
	"""


    d = {}
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] % 2 == 0:
            return False
    return True


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
