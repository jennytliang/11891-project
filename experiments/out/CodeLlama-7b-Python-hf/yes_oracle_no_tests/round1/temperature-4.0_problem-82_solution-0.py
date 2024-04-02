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

    x = len(string)
    if x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29:
        return True
    elif x > 2 and x % 2 == 0 or x > 3 and x % 3 == 0 or x > 5 and x % 5 == 0 or x > 7 and x % 7 == 0 or x > 11 and x % 11 == 0 or x > 13 and x % 13 == 0 or x > 17 and x % 17 == 0 or x > 19 and x % 19 == 0 or x > 23 and x % 23 == 0 or x > 29 and x % 29 == 0:
        return False
    else:
        return True


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
