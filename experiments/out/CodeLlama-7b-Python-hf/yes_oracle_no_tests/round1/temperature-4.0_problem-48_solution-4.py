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


def is_palindrome_better(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_better('')
    True
    >>> is_palindrome_better('aba')
    True
    >>> is_palindrome_better('aaaaa')
    True
    >>> is_palindrome_better('zbcd')
    False
    
	Include these tokens in the code:
		text == text[ : : - 1 ]
		text.lower()
		text.replace( ' ' , '' )
    """
    return text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]


def is_palindrome_best(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_best('')
    True
    >>> is_palindrome_best('aba')
    True
    >>> is_palindrome_best('aaaaa')
    True
    >>> is_palindrome_best('zbcd')
    False
    
	Include these tokens in the code:
		text.lower()
		text.replace( ' ' , '' )
		text.replace( '.' , '' )
		text.replace( ',' , '' )
		text.replace( '?' , '' )
		text.replace( '!' , '' )
		text.replace( ' ' , '' )
		text.replace( '-' , '' )
		text.replace( '\n' , '' )
		text.replace( '\t' , '' )
    """
    text = text.lower().replace(" ", "").replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("-", "").replace("\n", "").replace("\t", "")
    return text == text[::-1]


def is_palindrome_list(text: str):
    """
    Checks if given string