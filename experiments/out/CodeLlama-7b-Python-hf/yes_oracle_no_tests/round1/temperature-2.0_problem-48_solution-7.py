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
    return text == text[::-1]


def is_palindrome_faster(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_faster('')
    True
    >>> is_palindrome_faster('aba')
    True
    >>> is_palindrome_faster('aaaaa')
    True
    >>> is_palindrome_faster('zbcd')
    False
    """
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
