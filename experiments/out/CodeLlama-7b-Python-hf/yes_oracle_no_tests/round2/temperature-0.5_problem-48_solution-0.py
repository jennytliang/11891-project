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
    
	Do not include these tokens in the code: def is _ pal ind rome _ with _
	"""


    return text == text[:len(text) // 2][::-1] + text[len(text) // 2:]


def is_palindrome_reverse(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_reverse('')
    True
    >>> is_palindrome_reverse('aba')
    True
    >>> is_palindrome_reverse('aaaaa')
    True
    >>> is_palindrome_reverse('zbcd')
    False
    
	Do not include these tokens in the code: def is _ pal ind rome _ with _
	"""


    return text == text[::-1]


def is_palindrome_list(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_list('')
    True
    >>> is_palindrome_list('aba')
    True
    >>> is_palindrome_list('aaaaa')
    True
    >>> is_palindrome_list('zbcd')
    False
    
	Do not include these tokens in the code: def is _ pal ind rome _ with _
	"""


    return text == text[::-1]


def is_palindrome_join(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_join('')
    True
    >>> is_palindrome_join('aba')
    True
    >>> is_palindrome_join('aaaaa')
    True
    >>> is_palindrome_join('zbcd')
    False
    
	Do not include these tokens in the code: def is _ pal ind rome _ with _
	"""


    return text == text[::-1]


def is_palindrome_join_reverse(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_join_reverse('')
    True
    >>> is_palindrome_join_reverse('aba')
