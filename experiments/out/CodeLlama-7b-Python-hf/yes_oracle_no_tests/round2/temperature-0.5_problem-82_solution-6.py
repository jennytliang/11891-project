def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: a
	Do not include these tokens in the code: string
	"""


    
    de_string = string.replace(" ", "")
    string_len = len(de_string)
    print(string_len)
    if string_len == 2:
        return True
    elif string_len == 1:
        return False
    else:
        if string_len % 2 == 0:
            return False
        else:
            for i in range(3, string_len, 2):
                if string_len % i == 0:
                    return False
                else:
                    return True



print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))