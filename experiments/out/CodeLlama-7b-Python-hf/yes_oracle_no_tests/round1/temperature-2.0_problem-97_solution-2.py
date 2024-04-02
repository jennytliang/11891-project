def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int ( str ( a )[ - 1 ])
	"""
    return int(str(a)[-1]) * int(str(b)[-1])


# print(multiply(148, 412))
# print(multiply(19, 28))
# print(multiply(2020, 1851))
# print(multiply(14, -15))


def reverse(a):
    """Complete the function that takes an integer as an argument and
    returns the reverse of the integer as a string.
    Assume the input is always valid.
    
	Include these tokens in the code: return str ( a )[ :: - 1]
	"""
    return str(a)[::-1]


# print(reverse(12345))


def is_even(a):
    """Complete the function that takes an integer as an argument and
    returns True if the integer is even, False if the integer is odd.
    Assume the input is always valid.
    
	Include these tokens in the code: return not a % 2
	"""
    return not a % 2


# print(is_even(12345))


def is_valid_parentheses(s):
    """Complete the function that takes a string as an argument and
    returns True if it contains valid parentheses, False otherwise.
    
	Include these tokens in the code: return len ( s ) % 2 == 0
	"""
    return len(s) % 2 == 0


# print(is_valid_parentheses("[()]"))
# print(is_valid_parentheses("[(])"))


def is_prime(a):
    """Complete the function that takes an integer as an argument and
    returns True if the integer is prime, False otherwise.
    
	Include these tokens in the code: return a == 2 or ( a % 2 and not ( 3 <= a <= 20 and a % 20 in [ 0, 1, 5, 7, 11, 13, 17, 19 ]))
	"""
   