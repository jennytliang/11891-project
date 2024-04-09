def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: if len
	"""
    # pass
    # prime_number = 1
    # for x in range(1, string):
    #     if string % x == 0:
    #         prime_number += 1
    # if prime_number == 1:
    #     return True
    # else:
    #     return False
    # return True if len(string) in range(2, len(string)) else False
    return True if len(string) in range(2, len(string)) else False


print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
