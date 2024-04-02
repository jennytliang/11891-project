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
    if text == text[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
