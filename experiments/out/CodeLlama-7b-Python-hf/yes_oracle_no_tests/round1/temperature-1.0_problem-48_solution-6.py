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
    
	"""

    return text == text[:len(text):-1]


def is_palindrome_slice(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_slice('')
    True
    >>> is_palindrome_slice('aba')
    True
    >>> is_palindrome_slice('aaaaa')
    True
    >>> is_palindrome_slice('zbcd')
    False
    
	"""

    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
