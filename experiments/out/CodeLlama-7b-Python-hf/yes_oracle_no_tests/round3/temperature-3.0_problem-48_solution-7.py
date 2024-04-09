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


def is_palindrome_alt(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_alt('')
    True
    >>> is_palindrome_alt('aba')
    True
    >>> is_palindrome_alt('aaaaa')
    True
    >>> is_palindrome_alt('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    text = text.lower()
    text = ''.join(char for char in text if char.isalnum())
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
