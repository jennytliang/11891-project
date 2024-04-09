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
	Do not include these tokens in the code: raise Not Im plement ed Error
	"""
    # pass
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
