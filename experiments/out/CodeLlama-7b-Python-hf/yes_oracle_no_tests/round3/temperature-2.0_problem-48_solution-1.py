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
    
	Include these tokens in the code: [ :: -
	Do not include these tokens in the code: [: :
	"""



    return text  == text[::-1]

print(is_palindrome(''))
print(is_palindrome('aba'))
print(is_palindrome('aaaaa'))
print(is_palindrome('zbcd'))