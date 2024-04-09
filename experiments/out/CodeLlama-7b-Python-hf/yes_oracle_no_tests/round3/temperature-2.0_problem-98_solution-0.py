def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    # Your code here
    c = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            c += 1
    return c


def is_valid(s):
    """
    Given a string s, return True if it is valid according to these rules:
    The string is valid if all the symbols are in a valid order
    The order of the symbols is defined as the following:
    all lowercase letters come before uppercase letters
    all lowercase letters come before digits
    all digits come before symbols
    all symbols come before spaces
    
    For example:
    is_valid('aF2$') returns True
    is_valid('AF 2') returns False
    
	Include these tokens in the code: is nt
	Do not include these tokens in the code: is valid
	"""
    # Your code here
    for i in range(len(s) - 1):
        if s[i].islower() and s[i + 1].isupper():
            return False
        if s[i].islower() and s[i + 1].isdigit():
            return False
        if s[i].isdigit() and s[i + 1].isalpha():
            return False
        if s[i].isdigit() and s[i + 1].isspace():
            return False
        if s[i].isspace() and s[i + 1].isspace():
            return False
    return True


def is_palindrome(s):
    """
    Given a string s, return True if it is a palindrome, False otherwise.
    Note that capital letters are letters, and lower-case letters are letters.
    
    For example:
    is_palindrome('noon') returns True
    is_palindrome('Racecar') returns True
    is_palindrome('dogs') returns False
    
	Include these tokens in the code: is nt
	Do not include these tokens in the code: is palindrome
	"""
    # Your code here
    return s == s[::-