def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    
	Include these tokens in the code: return text == text [ :: - 1 ]
	"""
    return text == text[::-1]
    

def is_palindrome_two(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    
	Include these tokens in the code: return text == text [ :: - 1 ]
	"""
    return text[::-1] == text
    
    
print(is_palindrome(''))
print(is_palindrome('aba'))
print(is_palindrome('aaaaa'))
print(is_palindrome('zbcd'))
print(is_palindrome_two(''))
print(is_palindrome_two('aba'))
print(is_palindrome_two('aaaaa'))
print(is_palindrome_two('zbcd'))

