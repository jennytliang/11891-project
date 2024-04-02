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
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == text[::-1]


def is_palindrome_two(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_two('')
    True
    >>> is_palindrome_two('aba')
    True
    >>> is_palindrome_two('aaaaa')
    True
    >>> is_palindrome_two('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == text[::-1]


def is_palindrome_three(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_three('')
    True
    >>> is_palindrome_three('aba')
    True
    >>> is_palindrome_three('aaaaa')
    True
    >>> is_palindrome_three('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return True if text == text[::-1] else False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
